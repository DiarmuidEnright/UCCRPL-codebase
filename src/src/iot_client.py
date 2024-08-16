import json
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

class IoTClient:
    def __init__(self, client_id, endpoint, cert_path, key_path, root_ca_path):
        self.client = AWSIoTMQTTClient(client_id)
        self.client.configureEndpoint(endpoint, 8883)
        self.client.configureCredentials(root_ca_path, key_path, cert_path)
        self.client.configureConnectDisconnectTimeout(10)
        self.client.configureMQTTOperationTimeout(5)

    def connect(self):
        self.client.connect()

    def publish(self, topic, payload):
        message = json.dumps(payload)
        self.client.publish(topic, message, 1)

    def subscribe(self, topic, callback):
        self.client.subscribe(topic, 1, callback)
