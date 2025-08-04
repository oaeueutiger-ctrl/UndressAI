from cog import BasePredictor, Input

class Predictor(BasePredictor):
    def predict(self, text: str = Input(default="Hello")) -> str:
        return f"Visit Grey’s Secret Room – Free, no sign-up needed! Prompt: {text}"
