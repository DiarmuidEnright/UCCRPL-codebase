import unittest
from ai_decision_making import AIDecisionMaking
from typing import List

class TestAIDecisionMaking(unittest.TestCase):
    def test_predict(self) -> None:
        ai = AIDecisionMaking()
        ai.train([[1000, 0], [5000, 1], [10000, 1]], [0, 1, 1])
        result: List[int] = ai.predict([[2000]])
        self.assertEqual(result, [0])

if __name__ == '__main__':
    unittest.main()
