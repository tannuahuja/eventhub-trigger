# Eventhub-trigger

previously, I have used blob trigger and http trigger which starts vm, when any video is uploaded and sends the hit to the backend API but this function is not working sometimes it is not sending hits.

## So we are using evethub trigger

 
#### Choose Event Hub Trigger if:
You need real-time processing of data.
You expect high-throughput and need to handle large volumes of events.
Your architecture benefits from decoupling between producers and consumers.
You need to support multiple consumers reacting to the same event stream.
You're working with streaming data or require event ordering.

#### Choose Blob Trigger if:
Your workflow revolves around file uploads or changes in Azure Blob Storage.
You need to process files in a batch-oriented manner.
Your application is simpler and doesn't require the scalability or complexity of an event streaming solution.




## error facing
Getting validation handshake failed exception while configuring webhook for event subscription
because of event subscription endpoint was wrong

https://learn.microsoft.com/en-us/azure/azure-functions/functions-event-grid-blob-trigger?pivots=programming-language-python





#[ https://learn.microsoft.com/en-us/answers/questions/1314474/getting-validation-handshake-failed-exception-whil](https://learn.microsoft.com/en-us/answers/questions/1314474/getting-validation-handshake-failed-exception-whil)
