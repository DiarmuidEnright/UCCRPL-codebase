import unittest
from unittest.mock import patch, call
from src import gpio_controller

class TestGPIOController(unittest.TestCase):

    @patch('src.gpio_controller.GPIO.output')
    @patch('src.gpio_controller.time.sleep')
    def test_trigger_delay_charge(self, mock_sleep, mock_output):
        gpio_controller.trigger_delay_charge()
        mock_output.assert_has_calls([call(gpio_controller.DELAY_CHARGE_PIN, True), 
                                      call(gpio_controller.DELAY_CHARGE_PIN, False)])
        mock_sleep.assert_called_once_with(2)

    @patch('src.gpio_controller.GPIO.output')
    @patch('src.gpio_controller.time.sleep')
    def test_release_parachute(self, mock_sleep, mock_output):
        gpio_controller.release_parachute()
        mock_output.assert_has_calls([call(gpio_controller.PARACHUTE_PIN, True), 
                                      call(gpio_controller.PARACHUTE_PIN, False)])
        mock_sleep.assert_called_once_with(1)

if __name__ == '__main__':
    unittest.main()
