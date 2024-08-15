import unittest
from ai_decision_making import AIDecisionMaking

class TestAIDecisionMaking(unittest.TestCase):
    def test_predict(self):
        ai = AIDecisionMaking()
        ai.train([[1000, 0], [5000, 1], [10000, 1]], [0, 1, 1])
        result = ai.predict([[2000]])
        self.assertEqual(result, [0])

if __name__ == '__main__':
    unittest.main()
