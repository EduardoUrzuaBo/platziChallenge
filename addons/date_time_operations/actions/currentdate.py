"""This module contains the CurrentDate proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class CurrentDate(ActionProxy):
    def __init__(self, format: str):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="9k_I6NoN_06CR22QXqBpAQ",
            classname="Actions.CurrentDate"
        )
        self.format = format
        self.result = None
