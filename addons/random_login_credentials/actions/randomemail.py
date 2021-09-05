"""This module contains the RandomEmail proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class RandomEmail(ActionProxy):
    def __init__(self, localPart: str, domain: str, isLower: bool, isUpper: bool, isSpecial: bool, localPartLength: int = 10):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="uhFWuHjwpU-gl6uzWR5TXA",
            classname="main.Addons.RandomEmail"
        )
        self.localPart = localPart
        self.domain = domain
        self.localPartLength = localPartLength
        self.isLower = isLower
        self.isUpper = isUpper
        self.isSpecial = isSpecial
        self.emailAddress = None
