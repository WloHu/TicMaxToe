import pytest

from src.board import Board

@pytest.fixture(scope="function")
def create_board():

    def _create_board(state):
        return Board(state=state)

    return _create_board


