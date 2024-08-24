import unittest
from unittest.mock import patch, MagicMock
from src.sensor_motor_dashboard import SensorMotorDashboard

class TestSensorMotorDashboard(unittest.TestCase):

    @patch('src.sensor_motor_dashboard.get_sensor_readings')
    def test_update_sensor_data(self, mock_get_sensor_readings: MagicMock) -> None:
        mock_get_sensor_readings.return_value = (1.0, 2.0, 3.0, 4.0, 5.0, 6.0)
        
        dashboard = SensorMotorDashboard()
        dashboard.update_sensor_data()

        self.assertEqual(dashboard.sensor_labels['Acceleration X'].cget('text'), "Acceleration X: 1.00")
        self.assertEqual(dashboard.sensor_labels['Gyroscope Z'].cget('text'), "Gyroscope Z: 6.00")

    @patch('src.sensor_motor_dashboard.Motor')
    def test_update_motor_stats(self, mock_motor: MagicMock) -> None:
        mock_motor_instance = mock_motor.return_value
        mock_motor_instance.power = 100.0
        mock_motor_instance.torque = 200.0
        mock_motor_instance.efficiency = 90.0
        mock_motor_instance.weight = 10.0

        dashboard = SensorMotorDashboard()
        dashboard.update_motor_stats()

        self.assertEqual(dashboard.motor_labels['Power'].cget('text'), "Power: 100.00 HP")
        self.assertEqual(dashboard.motor_labels['Torque'].cget('text'), "Torque: 200.00 Nm")

    @patch('src.sensor_motor_dashboard.authenticate')
    @patch('src.sensor_motor_dashboard.trigger_delay_charge')
    def test_trigger_delay_charge_authorized(self, mock_trigger_delay_charge: MagicMock, mock_authenticate: MagicMock) -> None:
        mock_authenticate.return_value = True
        dashboard = SensorMotorDashboard()
        dashboard.is_authorized = False
        dashboard.trigger_delay_charge()
        self.assertTrue(dashboard.is_authorized)
        mock_trigger_delay_charge.assert_called_once()

    @patch('src.sensor_motor_dashboard.authenticate')
    @patch('src.sensor_motor_dashboard.release_parachute')
    def test_release_parachute_authorized(self, mock_release_parachute: MagicMock, mock_authenticate: MagicMock) -> None:
        mock_authenticate.return_value = True
        dashboard = SensorMotorDashboard()
        dashboard.is_authorized = False
        dashboard.release_parachute()
        self.assertTrue(dashboard.is_authorized)
        mock_release_parachute.assert_called_once()

if __name__ == '__main__':
    unittest.main()
