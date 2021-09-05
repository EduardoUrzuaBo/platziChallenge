"""This module contains the GetCurrentDate proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class GetCurrentDate(ActionProxy):
    def __init__(self, timeZone: str):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="9k_I6NoN_06CR22QXqBpAQ",
            classname="Actions.GetCurrentDate"
        )
        self.result = None
        self.timeZone = timeZone
