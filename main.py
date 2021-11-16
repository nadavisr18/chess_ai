from board.board import Board

if __name__ == "__main__":
    b = Board()
    starting_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
    fen = "rnbqkbnr/1ppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"

    b.fen_to_board(fen)
    b.display()

    b.allowed_moves(b.board_list[0][0])

