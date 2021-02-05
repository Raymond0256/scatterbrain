"""Note entry with metadata."""
from datetime import datetime
from os import getlogin


class Note():
    """Note entry with metadata."""

    def __init__(self, content: str, author: str) -> None:
        """Initializer or Note class."""
        self._content = content
        self._author = getlogin()
        self._date = datetime.now()

    def update_note(self, updated_content) -> None:
        """Update the content of a note."""
        if self._content not in updated_content:
            self._buffer = self._content
        self._content = updated_content
