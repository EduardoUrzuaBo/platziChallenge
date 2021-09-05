"""This module contains the ClearContentsIfVisibleWeb proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class ClearContentsIfVisibleWeb(ActionProxy):
    def __init__(self, timeout: str):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="inW2AJJ04ku45E9-RN2zqA",
            classname="io.testproject.addon.ClearContentsActions.ClearContentsIfVisibleWeb"
        )
        self.timeout = timeout
