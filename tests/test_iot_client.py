import unittest
from unittest.mock import patch
from iot_client import IoTClient

class TestIoTClient(unittest.TestCase):
    @patch('AWSIoTPythonSDK.MQTTLib.AWSIoTMQTTClient.connect')
    def test_connect(self, mock_connect: unittest.mock.MagicMock) -> None:
        client = IoTClient("testClient", "endpoint", "cert.pem", "private.key", "root-ca.pem")
        client.connect()
        mock_connect.assert_called_once()

if __name__ == '__main__':
    unittest.main()
