import pytest

from src.board import Board
from src.node import Node

BOARD_STATES = (
    ['X', 'O', None, None, None, None, 'X', 'O', 'X'],
    ['O', 'O', 'X', 'X', 'X', 'O', 'X', 'X', None],
    ['O', 'X', 'O', 'X', 'X', 'O', 'X', 'O', 'X']
)

IS_TERMINAL_EXPECTED = (
    False,
    True,
    True
)

EXPECTED_CALC = (
    None,
    50,
    0
)


@pytest.mark.parametrize("state", BOARD_STATES)
def test_gen_children(create_board, state):
    node = Node(create_board(state), prev_piece='X', next_piece='O')
    node.gen_children()

    print(node.board)
    if not node.board.possible_moves():
        assert node.children == None
    else:
        assert len(node.children) == len(node.board.possible_moves())
        for elem in node.children:
            print(elem.board)
            print(elem.resulting_move)
            assert elem.next_piece == node.prev_piece
            assert elem.prev_piece == node.next_piece

@pytest.mark.parametrize("state, expected", zip(BOARD_STATES, IS_TERMINAL_EXPECTED))
def test_is_terminal(create_board, state, expected):
    node = Node(create_board(state), prev_piece='X', next_piece='O')
    node.gen_children()

    assert node.is_terminal() == expected

@pytest.mark.parametrize("state, expected", zip(BOARD_STATES, EXPECTED_CALC))
def test_calc_value(create_board, state, expected):
    node = Node(create_board(state), prev_piece='X', next_piece='O')
    node.gen_children()
    if not node.is_terminal():
        assert pytest.raises(AssertionError)
    else:
        node.calc_value(True, 0)
        assert node.value == expected



