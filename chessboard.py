def print_chessboard():
    board = ""
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                board += "■ "
            else:
                board += "□ "
        board += "\n"
    print(board)

if __name__ == "__main__":
    print_chessboard()