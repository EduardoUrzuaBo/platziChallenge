"""This module contains the CurrentTimestamp proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class CurrentTimestamp(ActionProxy):
    def __init__(self):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="9k_I6NoN_06CR22QXqBpAQ",
            classname="Actions.CurrentTimestamp"
        )
        self.result = None
