import string
import random

from .actions import RandomEmail, RandomPassword, RandomUsername


class RandomLoginCredentials:
    @staticmethod
    def randomemail(localPart: str, domain: str, isLower: bool, isUpper: bool, isSpecial: bool, localPartLength: int) -> RandomEmail:
        """Generate random email address."""
        return RandomEmail(localPart, domain, isLower, isUpper, isSpecial, localPartLength)

    @staticmethod
    def randompassword(passwordLength: int, specialCharacters: bool, digits: bool, upperCase: bool, lowerCase: bool) -> RandomPassword:
        """Generate random password."""
        return RandomPassword(passwordLength, specialCharacters, digits, upperCase, lowerCase)

    @staticmethod
    def randomusername(length: int) -> RandomUsername:
        """Generate random username."""
        return RandomUsername(length)

    @staticmethod
    def random_char(y):
        return ''.join(random.choice(string.ascii_letters) for x in range(y))


