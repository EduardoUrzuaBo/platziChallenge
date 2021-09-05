"""This module contains the GetHourInStringFormat proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class GetHourInStringFormat(ActionProxy):
    def __init__(self, dateTimeValue: str, dateTimeFormat: str, suffix: bool):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="9k_I6NoN_06CR22QXqBpAQ",
            classname="Actions.Getters.Hours.GetHourInStringFormat"
        )
        self.dateTimeValue = dateTimeValue
        self.dateTimeFormat = dateTimeFormat
        self.suffix = suffix
        self.result = None
