#!/usr/bin/env python
import pika
import sys

url = 'amqp://lvfqbbym:hZBmLLY4OVCWRbIHjXpKPr9XUNTcufcz@clam.rmq.cloudamqp.com/lvfqbbym'
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs',
                         exchange_type='topic')

routing_key = sys.argv[1] if len(sys.argv) > 2 else 'anonymous.info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'
channel.basic_publish(exchange='topic_logs',
                      routing_key=routing_key,
                      body=message)
print(" [x] Sent %r:%r" % (routing_key, message))
connection.close()
