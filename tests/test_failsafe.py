import unittest
from unittest.mock import patch, MagicMock
from src import failsafe

class TestFailsafe(unittest.TestCase):

    @patch('src.failsafe.get_altitude')
    @patch('src.failsafe.release_parachute')
    def test_monitor_altitude_threshold_met(self, mock_release_parachute: MagicMock, mock_get_altitude: MagicMock) -> None:
        mock_get_altitude.return_value = 900
        failsafe.monitor_altitude()
        mock_release_parachute.assert_called_once()

    @patch('src.failsafe.get_altitude')
    @patch('src.failsafe.release_parachute')
    def test_monitor_altitude_threshold_not_met(self, mock_release_parachute: MagicMock, mock_get_altitude: MagicMock) -> None:
        mock_get_altitude.return_value = 1100
        failsafe.monitor_altitude()
        mock_release_parachute.assert_not_called()

if __name__ == '__main__':
    unittest.main()

