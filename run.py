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


    def board_size():
        pass

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

    def guess_ship_location():
        pass

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

    def game_over_message():
        pass

    def is_game_over():
        pass

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