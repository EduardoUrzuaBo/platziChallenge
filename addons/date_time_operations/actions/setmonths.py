"""This module contains the SetMonths proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class SetMonths(ActionProxy):
    def __init__(self, months: str, originalDateTimeValue: str, originalDateTimeFormat: str, resultFormat: str):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="9k_I6NoN_06CR22QXqBpAQ",
            classname="Actions.Setters.SetMonths"
        )
        self.months = months
        self.originalDateTimeValue = originalDateTimeValue
        self.originalDateTimeFormat = originalDateTimeFormat
        self.resultFormat = resultFormat
        self.result = None
