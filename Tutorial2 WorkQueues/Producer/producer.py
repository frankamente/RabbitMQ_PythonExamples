#!/usr/bin/env python
import pika
import sys

message = ' '.join(sys.argv[1:]) or "Hello World!"
concatenateMessage = ''
url = 'amqp://lvfqbbym:hZBmLLY4OVCWRbIHjXpKPr9XUNTcufcz@clam.rmq.cloudamqp.com/lvfqbbym'
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()
for counter in range(1):
    concatenateMessage = message + str(counter) + concatenateMessage
    channel.basic_publish(exchange='test-exchange-fanout', routing_key='red',
                          body=concatenateMessage,
                          properties=pika.BasicProperties(
                              delivery_mode=2,  # make message persistent
                          ))
    print("Sent %r" % concatenateMessage)
