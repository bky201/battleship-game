from random import randint

class BattleShipGame:
    def __init__(self):
        self.board_size = 0
        self.player_score = 0
        self.computer_score = 0
        self.Hidden_Pattern_Player = []
        self.Hidden_Pattern_Computer = []
        self.Guess_Pattern_Player = []
        self.Guess_Pattern_Computer = []
        self.player_guessed_locations = []
        self.computer_guessed_locations = []


    def get_board_size(self):
        """
        Prompts the user to enter the board size and validates the input.

        Returns:
            int: The validated board size.
        """
        while True:
            size = input("Enter the board size (minimum 4): ")
            if size.isdigit():
                size = int(size)
                if size >= 4:
                    return size
            print("Invalid board size. Please enter a number greater than or equal to 5.")


    def ship_numbers():
        pass

    def print_game_board(self, board):
        """
        Prints the game board.

        Args:
            board (list): The game board to print.
        """
        print(' ' + ' '.join([str(i) for i in range(1, self.board_size + 1)]))
        for i, row in enumerate(board):
            print(str(i + 1) + '|' + '|'.join(row) + '|')

    def is_valid_input(self, value):
        """
        Checks if the input value is valid.

        Args:
            value (str): The input value to check.

        Returns:
            bool: True if the input value is valid, False otherwise.
        """
        return value in [str(i) for i in range(1, self.board_size +1)]

    def get_unique_ship_location(self, guessed_locations):
        """
        Gets a unique ship location from the user.
        Args:
            guessed_locations (list): The list of already guessed locations.
        Returns:
            tuple: The row and column indices of the ship location.
                    Returns None if all possible guesses have been made.
        """
        num_rows = len(self.Hidden_Pattern_Player)
        num_cols = len(self.Hidden_Pattern_Computer)
        max_guesses = num_rows * num_cols

        num_guesses = len(guessed_locations)
        if num_guesses >= max_guesses:
            print("You have made all possible guesses. The game is over.")
            return None
        
        while True:
            try:
                row = int(input(f'\nPlease enter a ship row 1-{num_rows}: '))
                column = int(input(f'Please enter a ship column 1-{num_cols}: '))

                if (
                    1 <= row <= num_rows
                    and 1 <= column <= num_cols
                    and (row - 1, column - 1) not in guessed_locations
                    and self.is_valid_input(str(row))
                    and self.is_valid_input(str(column))
                ):
                    return row - 1, column - 1
                else:
                    print("Invalid input or location already guessed. Please enter valid coordinates.")
            except ValueError:
                print("Invalid input. Please enter valid coordinates.")


    def create_ships(self, board):
        """
        Randomly creates ships on the game board.

        Args:
            board (list): The game board to create ships on.
        """
        num_ships = self.board_size

        ship_locations = set()
        for i in range(num_ships):
            while True:
                #Generate random ship location
                ship_r, ship_c = randint(0, self.board_size - 1), randint(0, self.board_size - 1)
                ship_location = (ship_r, ship_c)
                if ship_location not in ship_locations:
                    ship_locations.add(ship_location)
                    #Place ship on the board
                    board[ship_r][ship_c] = "$"
                    break

    def print_score(self):
        """
        Prints the current scores of the players.
        """
        print("\nPlayer Score:", self.player_score)
        print("Computer Score:", self.computer_score)

    def count_hits(self, board):
        """
        Counts the number of hits on the game board.

        Args:
            board (list): The game board to count hits on.

        Returns: 
            int: The number of hits.
        """

        count = 0
        for row in board:
            for column in row:
                if column == "#":
                    count += 1
        return count

    def game_over_message(self, result):
        """
        Prints the game over message based on the result.

        Args:
            result (str): The result of the game ('Player' or 'Computer').
        """
        if result == 'Player':
            print("\nCongratulations! You win!")
        elif result == 'Computer':
            print("\nGame Over. Computer wins!")

    def is_game_over(self):
        """
        Checks if the game is over.

        Returns:
            bool: True if the game is over, False otherwise.
        """
        num_ships = self.board_size
        return self.player_score >= num_ships or self.computer_score >= num_ships

    def computer_guess():
        pass

    def play(self):
        """
        Starts the Battleship game.
        """
        print("\nLet's play Battleship!                   ")
        print("The '$' represents the hidden battleships. ")
        print("The '#' represents a hit.                  ")
        print("The '0' represents a miss.                 ")
        print("The 'x' represents a player's missed guess.")
        print("Good luck!\n                               ")

        self.board_size = self.get_board_size()
        self.Hidden_Pattern_Player = [['-']*self.board_size for _ in range(self.board_size)]
        self.Hidden_Pattern_Computer = [['-']*self.board_size for _ in range(self.board_size)]
        self.Guess_Pattern_Player = [['-']*self.board_size for _ in range(self.board_size)]
        self.Guess_Pattern_Computer = [['-']*self.board_size for _ in range(self.board_size)]

        self.create_ships(self.Hidden_Pattern_Player)
        self.create_ships(self.Hidden_Pattern_Computer)

        print("\nPlayer Board:")
        self.print_game_board(self.Guess_Pattern_Player)


        print("\nComputer Board:")
        self.print_game_board(self.Guess_Pattern_Computer)


    def game_home_page(self):
        pass


if __name__ == '__main__':
    game = BattleShipGame()
    game.game_home_page()