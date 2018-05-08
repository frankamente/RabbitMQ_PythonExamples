#!/usr/bin/env python
import pika
import sys

message = ' '.join(sys.argv[1:]) or "Hello World!"
concatenateMessage = ''
url = 'amqp://lvfqbbym:hZBmLLY4OVCWRbIHjXpKPr9XUNTcufcz@clam.rmq.cloudamqp.com/lvfqbbym'
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',
                         exchange_type='direct')

severity = sys.argv[1] if len(sys.argv) > 2 else 'info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'
channel.basic_publish(exchange='direct_logs',
                      routing_key=severity,
                      body=message)
print(" [x] Sent %r:%r" % (severity, message))
connection.close()
