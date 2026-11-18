# RabbitMQ

## Questions
What is the difference between a producer, a queue and a consumer?
Producer published message, queue holds them, consumer receives them.

When the worker was stopped, why did the Ready count increase?
no consumer to receive the message, back to ready state

What changed in RabbitMQ Management while the worker was processing a message?
message moved from ready to unacked, once acked, unacked decreased.

What does HTTP 202 Accepted tell the client, and what does it not guarantee?
202 means the request was accepted, but doesnt mean it was processed successfully

Why is await useful when a FastAPI endpoint communicates with RabbitMQ?
other tasks can run instead while waiting

What changed when you set prefetch_count=2? Did the worker actually process two orders at the same time?
just enabled 2 unacked messages max at a time per worker. the worker doesnt process 2 orders at the same time. 

With two consumers using prefetch_count=1, what did the Consumers and Unacknowledged counts show?
for 2 messages Consumers: 2, Unacked: 2 as both can process at same time

What happened when one worker stopped before acknowledging an order? Why can the same message be delivered twice?
unacked message can be requeued, same msg can be delivered twice if worker failed before ack was received

In your own words, what does an event loop do while an async function is awaiting a network operation?
the event loop lets other tasks run while one task is waiting for a network operation