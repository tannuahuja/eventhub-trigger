import logging
import requests
import azure.functions as func

app = func.FunctionApp()

# Function to send data to the backend API
def send_data_to_api(video_name, video_path):
    retries = 7
    for attempt in range(retries):
        try:
            post_data = {
                "server_status": "running",
                "video_status": "uploaded",
                "video_name": video_name,
                "video_path": video_path,
            }
            logging.debug(f"Sending data to API: {post_data}")
            response = requests.post(
                "http://20.219.219.69:8076/api/session/available",
                json=post_data,
                timeout=10
            )
            response.raise_for_status()
            logging.info(f"Notification sent successfully. Status Code: {response.status_code}")
            return
        except requests.exceptions.RequestException as e:
            logging.error(f"API request failed on attempt {attempt + 1}: {e}")

# Event Grid Trigger Function
@app.function_name(name="EventGridTriggerFunction")
@app.event_grid_trigger(arg_name="azeventgrid")
def event_grid_trigger_function(azeventgrid: func.EventGridEvent):
    logging.info('Python EventGrid trigger processed an event')
    
    # Extract event data
    event_data = azeventgrid.get_json()
    event_type = event_data.get('eventType')

    # Check if the event type is Blob Created
    if event_type == "Microsoft.Storage.BlobCreated":
        blob_url = event_data.get('data', {}).get('url')
        blob_name = event_data.get('data', {}).get('name')
        
        logging.info(f"Blob created: {blob_name}")
        logging.info(f"Blob URL: {blob_url}")
        
        # Send notification to the backend
        send_data_to_api(blob_name, blob_url)
    else:
        logging.warning(f"Unhandled event type: {event_type}")
