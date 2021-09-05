"""This module contains the RandomPassword proxy action class."""
from distutils.util import strtobool

from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class RandomPassword(ActionProxy):
    def __init__(self, passwordLength: int = 8, specialCharacters: bool = bool(strtobool('true')), digits: bool = bool(strtobool('true')), upperCase: bool = bool(strtobool('true')), lowerCase: bool = bool(strtobool('true'))):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="uhFWuHjwpU-gl6uzWR5TXA",
            classname="main.Addons.RandomPassword"
        )
        self.passwordLength = passwordLength
        self.specialCharacters = specialCharacters
        self.digits = digits
        self.upperCase = upperCase
        self.lowerCase = lowerCase
        self.generatedPassword = None
