"""This module contains the GetDateInFormat proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class GetDateInFormat(ActionProxy):
    def __init__(self, currentDateTimeValue: str, currentDateTimeFormat: str, expectedDateTimeFormatFormat: str, locale: str):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="9k_I6NoN_06CR22QXqBpAQ",
            classname="Actions.FormatDate.GetDateInFormat"
        )
        self.currentDateTimeValue = currentDateTimeValue
        self.currentDateTimeFormat = currentDateTimeFormat
        self.expectedDateTimeFormatFormat = expectedDateTimeFormatFormat
        self.locale = locale
        self.result = None
