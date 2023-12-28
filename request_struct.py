from typing import TypedDict

class RatesRequestClass:
    def __init__(self):
        self.success = True
        self.timestamp = ''
        self.date = ''
        self.rates = dict(nis=0.01)