"""This module contains the GetHoursBetweenTwoDates proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class GetHoursBetweenTwoDates(ActionProxy):
    def __init__(self, firstDateTime: str, firstDateTimeFormat: str, secondDateTime: str, secondDateTimeFormat: str):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="9k_I6NoN_06CR22QXqBpAQ",
            classname="Actions.DurationBetweenDates.GetHoursBetweenTwoDates"
        )
        self.firstDateTime = firstDateTime
        self.firstDateTimeFormat = firstDateTimeFormat
        self.secondDateTime = secondDateTime
        self.secondDateTimeFormat = secondDateTimeFormat
        self.result = None
