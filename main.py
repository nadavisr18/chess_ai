from board.board import Board

if __name__ == "__main__":
    b = Board()
    starting_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
    fen = "rnbqkbnr/p1pppppp/8/8/1p6/P7/1PPPPPPP/RNBQKBNR"

    b.fen_to_board(starting_fen)
    b.display()

    b.allowed_moves(b.board_list[5][0])

