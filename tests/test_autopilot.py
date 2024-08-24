import unittest
from autopilot import Autopilot

class TestAutopilot(unittest.TestCase):
    
    def test_next_waypoint(self) -> None:
        autopilot = Autopilot([1000, 2000, 3000])
        self.assertEqual(autopilot.next_waypoint(), 1000)
        self.assertEqual(autopilot.next_waypoint(), 2000)
        self.assertEqual(autopilot.next_waypoint(), 3000)

if __name__ == '__main__':
    unittest.main()
