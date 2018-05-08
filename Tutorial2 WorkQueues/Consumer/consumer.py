#!/usr/bin/env python
import pika
import time

url = 'amqp://lvfqbbym:hZBmLLY4OVCWRbIHjXpKPr9XUNTcufcz@clam.rmq.cloudamqp.com/lvfqbbym'
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='test-queue', durable=True)


def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)
    time.sleep(body.count('.'))
    print " [x] Done"
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(callback, queue='test-queue')
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
