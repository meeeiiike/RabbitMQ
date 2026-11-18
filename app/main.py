import os
import aio_pika
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

load_dotenv()
RABBIT_URL = os.getenv("RABBIT_URL")
                       
app = FastAPI(title="RabbitMQ Lab 7")

class OrderRequest(BaseModel):
    order_id: int
    product: str
    quantity: int

@app.post("/orders", status_code=202)
async def submit_order(order: OrderRequest):
    connection = await aio_pika.connect_robust(RABBIT_URL)
    async with connection:
        channel = await connection.channel(publisher_confirms=True)
        queue = await channel.declare_queue("orders_queue", durable=True)
        message = aio_pika.Message(
            body=order.model_dump_json().encode(),
            content_type="application/json",
            delivery_mode=aio_pika.DeliveryMode.PERSISTENT,
        )
        await channel.default_exchange.publish(message, routing_key=queue.name)
    return {"status": "queued", "order_id": order.order_id}
