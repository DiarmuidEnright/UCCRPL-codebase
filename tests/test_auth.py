import unittest
from src import auth

class TestAuth(unittest.TestCase):

    def test_authenticate_success(self):
        self.assertTrue(auth.authenticate('admin', 'password'))

    def test_authenticate_failure(self):
        self.assertFalse(auth.authenticate('admin', 'wrongpassword'))
        self.assertFalse(auth.authenticate('unknownuser', 'password'))

if __name__ == '__main__':
    unittest.main()
