import unittest
from rth import ReturnToHome

class TestRTH(unittest.TestCase):
    def test_calculate_vector(self):
        rth = ReturnToHome((40.748817, -73.985428))
        self.assertIsNotNone(rth.calculate_vector((40.748800, -73.985400)))

if __name__ == '__main__':
    unittest.main()
