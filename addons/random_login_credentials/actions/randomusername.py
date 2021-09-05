"""This module contains the RandomUsername proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class RandomUsername(ActionProxy):
    def __init__(self, length: int = 6):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="uhFWuHjwpU-gl6uzWR5TXA",
            classname="main.Addons.RandomUsername"
        )
        self.length = length
        self.result = None
