import json
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from typing import Callable, Any

class IoTClient:
    def __init__(self, client_id: str, endpoint: str, cert_path: str, key_path: str, root_ca_path: str) -> None:
        self.client: AWSIoTMQTTClient = AWSIoTMQTTClient(client_id)
        self.client.configureEndpoint(endpoint, 8883)
        self.client.configureCredentials(root_ca_path, key_path, cert_path)
        self.client.configureConnectDisconnectTimeout(10)
        self.client.configureMQTTOperationTimeout(5)

    def connect(self) -> None:
        self.client.connect()

    def publish(self, topic: str, payload: Any) -> None:
        message: str = json.dumps(payload)
        self.client.publish(topic, message, 1)

    def subscribe(self, topic: str, callback: Callable[[Any], None]) -> None:
        self.client.subscribe(topic, 1, callback)
