"""Note entry with metadata."""


class Note():
    """Note entry with metadata."""

    def __init__(self, content: str, author: str, date: str) -> None:
        """Initializer or Note class."""
        self._content = content
        self._author = author
        self._date = date
