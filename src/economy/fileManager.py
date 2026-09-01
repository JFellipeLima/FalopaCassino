'''Responsável pelo gerenciamento do arquivo JSON'''

import json
import os

class Files:
    def __init__(self):
        self.DATA_PATH = os.path.join(
            os.path.dirname(__file__),
            "..",
            "data",
            "data.json"
        )

    def load(self):
        if not os.path.exists(self.DATA_PATH):
            return None

        with open(self.DATA_PATH, "r", encoding="utf-8") as file:
            data = json.load(file)

        return data

    def save(self, user):
        os.makedirs(os.path.dirname(self.DATA_PATH), exist_ok=True)

        with open(self.DATA_PATH, "w", encoding="utf-8") as file:
            json.dump(user, file, indent=4)
