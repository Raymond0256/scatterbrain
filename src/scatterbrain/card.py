"""Task Card Class."""
from datetime import datetime


class Card():
    """Task Card for tracking project task information."""

    def __init__(self, title: str) -> None:
        """Initializer for Task Card."""
        self._title: str = title
        self._description = ""
    
    def add_due_date(self, due_date: datetime) -> None:
        """Add a due date to the card."""
        self._due_date = due_date
