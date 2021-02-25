from board.board import Board

if __name__ == "__main__":
    b = Board()

    fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"

    b.fen_to_board(fen)
    b.display()

    b.allowed_moves(b.board_list[6][0])

