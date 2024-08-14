import unittest
from unittest.mock import patch, MagicMock
from src import failsafe

class TestFailsafe(unittest.TestCase):

    @patch('src.failsafe.get_altitude')
    @patch('src.failsafe.release_parachute')
    def test_monitor_altitude_threshold_met(self, mock_release_parachute, mock_get_altitude):
        mock_get_altitude.return_value = 900  # Below the threshold
        failsafe.monitor_altitude()
        mock_release_parachute.assert_called_once()

    @patch('src.failsafe.get_altitude')
    @patch('src.failsafe.release_parachute')
    def test_monitor_altitude_threshold_not_met(self, mock_release_parachute, mock_get_altitude):
        mock_get_altitude.return_value = 1100  # Above the threshold
        failsafe.monitor_altitude()
        mock_release_parachute.assert_not_called()

if __name__ == '__main__':
    unittest.main()
