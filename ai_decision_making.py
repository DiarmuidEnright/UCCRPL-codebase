from sklearn.linear_model import LogisticRegression

class AIDecisionMaking:
    def __init__(self, model=None):
        self.model = model or LogisticRegression()

    def train(self, training_data, labels):
        self.model.fit(training_data, labels)

    def predict(self, input_data):
        return self.model.predict(input_data)
