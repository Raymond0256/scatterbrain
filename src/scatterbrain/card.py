"""Task Card Class."""


class Card():
    """Task Card for tracking project task information."""

    def __init__(self, title: str) -> None:
        """Initializer for Task Card."""
        self._title = title
