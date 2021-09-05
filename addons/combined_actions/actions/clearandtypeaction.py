"""This module contains the ClearAndTypeAction proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class ClearAndTypeAction(ActionProxy):
    def __init__(self, keys: str):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="LFtMVbTf9EW7YK8qK4xzlQ",
            classname="io.testproject.addon.combined.actions.ClearAndTypeAction"
        )
        self.keys = keys
