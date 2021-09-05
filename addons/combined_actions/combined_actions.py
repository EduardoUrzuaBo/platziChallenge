from .actions import ClearAndTypeAction


class CombinedActions:
    @staticmethod
    def clearandtypeaction(keys: str) -> ClearAndTypeAction:
        """Run Clear {{element}} contents and type {{keys}}."""
        return ClearAndTypeAction(keys)
