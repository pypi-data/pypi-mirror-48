import pika
import uuid
import os
import json
from pprint import pprint

class Abstract_Service (object):
    
    def __init__(self, routing_key = None):
        
        url = os.environ.get('CLOUDAMQP_URL', 'amqp://snfsdfuv:wYirfMCCAJ29qtBKVH3pbwMbNcshLfYZ@barnacle.rmq.cloudamqp.com/snfsdfuv')
        params = pika.URLParameters(url)
        self.connection = pika.BlockingConnection(params)
        self.channel = self.connection.channel()
        self.routing_key = routing_key    
        result = self.channel.queue_declare(exclusive=True)

        pprint(self.routing_key)

        self.callback_queue = result.method.queue
        self.channel.basic_consume(self.on_response, 
                                    no_ack=True,
                                    queue=self.callback_queue)
    
    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def integrate(self, user_key, tfs_url, organization_url):

        data = {'key': user_key, 
                'tfs_url': tfs_url,
                'organization_url': organization_url}       
        
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',
                                   routing_key=self.routing_key,
                                   properties=pika.BasicProperties(
                                         reply_to = self.callback_queue,
                                         correlation_id = self.corr_id,
                                         content_type = "application/json"
                                         ),
                                   body=json.dumps(data))
        
        while self.response is None:
            self.connection.process_data_events()
        return self.response