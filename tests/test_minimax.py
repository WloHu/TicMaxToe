import pytest

from src.minimax import Minimax
from src.node import Node
from src.board import Board

BOARD_STATE = (
    ['O', 'X', None, 'O', None, None, None, None, None],
    ['O', 'X', None, 'O', 'X', None, None, None, None],
    ['X', 'O', 'O', None, 'O', 'X', None, 'X', None],
    ['X', None, None, None, 'X', 'O', 'O', None, None]

)
EXPECTED = (6, 7, 6 ,8)

@pytest.mark.parametrize("state, expected", zip(BOARD_STATE, EXPECTED))
def test_minimax(create_board, state, expected):
    board = create_board(state)
    node = Node(board, 'O', 'X')
    minimax = Minimax(node)
    assert minimax.evaluate() == expected


