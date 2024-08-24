from sklearn.linear_model import LogisticRegression
from sklearn.base import BaseEstimator
from typing import Optional, Any, Union
import numpy as np

class AIDecisionMaking:
    def __init__(self, model: Optional[BaseEstimator] = None) -> None:
        self.model: BaseEstimator = model or LogisticRegression()

    def train(self, training_data: np.ndarray, labels: np.ndarray) -> None:
        self.model.fit(training_data, labels)

    def predict(self, input_data: np.ndarray) -> Union[np.ndarray, Any]:
        return self.model.predict(input_data)
