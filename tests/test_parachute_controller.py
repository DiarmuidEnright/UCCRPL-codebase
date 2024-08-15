import unittest
from unittest.mock import patch
from parachute_controller import ParachuteController

class TestParachuteController(unittest.TestCase):
    @patch('RPi.GPIO.output')
    def test_release_parachute(self, mock_output):
        controller = ParachuteController(17)
        controller.release_parachute()
        self.assertEqual(mock_output.call_count, 2)

if __name__ == '__main__':
    unittest.main()
