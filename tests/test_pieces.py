import pytest
from src.pieces import Pieces

def test_pieces():
    assert str(Pieces.X) == 'X'
    assert str(Pieces.O) == 'O'
    with pytest.raises(AttributeError):
        Pieces.Z

