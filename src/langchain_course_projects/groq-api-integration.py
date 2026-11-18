import os

class ChatGroq:
    """Moke ChatGroq class for education purposes."""
    def __init__(self,model,temperture=0,max_retries=2):
        self.model = model
        self.temperture = temperture
        self.max_retries = max_retries
        self.valid_models = [
            "llama-4.8b-instant",
            "llama-4.8b-instant",
            "llama-4.8b-instant"
        ]
        if model not in self.valid_models:
            raise ValueError(f"Invalid model:{model}")