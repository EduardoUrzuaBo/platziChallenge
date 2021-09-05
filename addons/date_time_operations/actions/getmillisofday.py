"""This module contains the GetMillisOfDay proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class GetMillisOfDay(ActionProxy):
    def __init__(self, dateTimeValue: str, dateTimeFormat: str):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="9k_I6NoN_06CR22QXqBpAQ",
            classname="Actions.Getters.Milliseconds.GetMillisOfDay"
        )
        self.dateTimeValue = dateTimeValue
        self.dateTimeFormat = dateTimeFormat
        self.result = None
