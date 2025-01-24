class Game:
    def __init__(self):
        """Initialize the game board and set the starting player."""
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

    def display_board(self):
        """Display the current state of the board."""
        for row in self.board:
            print(" | ".join(row))
            print("-" * 5)

    def make_move(self, row, col):
        """
        Make a move on the board if the position is valid and available.
        Args:
            row (int): The row index (0-2).
            col (int): The column index (0-2).
        Returns:
            bool: True if the move was valid, False otherwise.
        """
        if 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            return True
        print("Invalid move. Try again.")
        return False

    def check_win(self):
        """Check if the current player has won the game."""
        # Check rows and columns
        for i in range(3):
            if all(self.board[i][j] == self.current_player for j in range(3)) or \
               all(self.board[j][i] == self.current_player for j in range(3)):
                return True

        # Check diagonals
        if all(self.board[i][i] == self.current_player for i in range(3)) or \
           all(self.board[i][2 - i] == self.current_player for i in range(3)):
            return True

        return False

    def switch_player(self):
        """Switch to the other player."""
        self.current_player = "O" if self.current_player == "X" else "X"

    def start_game(self):
        """Start the main game loop."""
        print("Welcome to Tic Tac Toe!")
        self.display_board()

        while True:
            try:
                move = input(f"Player {self.current_player}, enter your move (row,col): ")
                row, col = map(int, move.split(","))
                if self.make_move(row, col):
                    self.display_board()
                    if self.check_win():
                        print(f"Player {self.current_player} wins!")
                        break
                    self.switch_player()
                else:
                    print("Move not valid.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter row,col (e.g., 1,1).")

            if all(cell != " " for row in self.board for cell in row):
                print("It's a draw!")
                break

# To run the game:
if __name__ == "__main__":
    game = Game()
    game.start_game()
