from src.board import Board
from src.pieces import Pieces
from src.players import AiPlayer, HumanPlayer

def test_creating_human_player():

    hplayer = HumanPlayer("X", Board())
    assert hplayer.piece == Pieces.X

def test_creating_Ai_player():

    state = [Pieces.O, Pieces.X, None, Pieces.O, None, None, None, None, None]
    board = Board(state=state)
    ai_player = AiPlayer(Pieces.X, board)
    assert ai_player._opponent_piece == Pieces.O
    ai_player.move()
    assert board.state[6] == Pieces.X

def test_simple_interaction():

    state = [None, Pieces.X, None, Pieces.O, None, None, None, None, None]
    board = Board(state=state)
    ai_player = AiPlayer(Pieces.X, board)
    h_player = HumanPlayer('O', board)
    assert h_player.board is ai_player.board
    h_player.move(0)
    ai_player.move()
    assert board.state[6] == Pieces.X
