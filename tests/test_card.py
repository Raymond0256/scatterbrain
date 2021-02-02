"""Test Card class."""
from scatterbrain.card import Card


import scatterbrain


def test_card_set_title():
    """Test Card class creation assigns title."""
    test_card = Card(title="test")
    assert test_card
    assert test_card.title = "test"
