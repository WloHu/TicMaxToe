import pytest

from src.board import Board

STATES = (
    ['X', 'X', 'X', None, 'O', None, 'O', None, None],
    ['O', 'O', 'O', None, 'X', None, 'X', None, None],
    ['O', None, None, None, 'O', 'X', 'X', None, 'O'],
    ['X', 'X', None, None, 'O', None, 'O', None, None],
    ['O', 'O', 'X', None, 'X', 'O', 'X', 'O', None],
    ['O', 'X', 'X', None, 'O', 'X', 'O', None, None],
)

WINNING_EXPECTATIONS = (True, True, True, False, True, False)

POSSIBLE_MOVES_EXPECTATIONS = (
    [3, 5, 7, 8],
    [3, 5, 7, 8],
    [1, 2, 3, 7],
    [2, 3, 5, 7, 8],
    [3, 8],
    [3, 7, 8]
)

@pytest.mark.parametrize("state, expected", zip(STATES, WINNING_EXPECTATIONS))
def test_is_winning(create_board, state, expected):

    board = create_board(state)
    assert board.is_winning() == expected


@pytest.mark.parametrize("state", STATES)
def test_copy_board(create_board, state):

    board_a = create_board(state)
    board_b = board_a.copy_board()

    assert id(board_a) != id(board_b)
    assert board_a is not board_b

@pytest.mark.parametrize("state, expected", zip(STATES, POSSIBLE_MOVES_EXPECTATIONS))
def test_possible_moves(create_board, state, expected):

    board = create_board(state)
    assert board.possible_moves() == expected

def test_make_move(create_board):

    board = create_board([None] * 9)
    board.make_move('X', 5)

    assert board.state[5] == 'X'
