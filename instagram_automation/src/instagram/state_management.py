
import json
import os

class StateManagement:

    def __init__(self, state_file='state.json'):
        self.state_file = state_file
        self.state = {}
        if os.path.exists(self.state_file):
            with open(self.state_file, 'r') as file:
                self.state = json.load(file)

    def get_state(self, key):
        return self.state.get(key)

    def set_state(self, key, value):
        self.state[key] = value
        with open(self.state_file, 'w') as file:
            json.dump(self.state, file)

    def delete_state(self, key):
        if key in self.state:
            del self.state[key]
            with open(self.state_file, 'w') as file:
                json.dump(self.state, file)
