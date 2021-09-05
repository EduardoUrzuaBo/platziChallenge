"""This module contains the SetSeconds proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class SetSeconds(ActionProxy):
    def __init__(self, seconds: str, originalDateTimeValue: str, originalDateTimeFormat: str, resultFormat: str):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="9k_I6NoN_06CR22QXqBpAQ",
            classname="Actions.Setters.SetSeconds"
        )
        self.seconds = seconds
        self.originalDateTimeValue = originalDateTimeValue
        self.originalDateTimeFormat = originalDateTimeFormat
        self.resultFormat = resultFormat
        self.result = None
