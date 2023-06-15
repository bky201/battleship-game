from random import randint
from colorama import Fore, Back, Style
from colorama import init
from termcolor import colored

init()

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
            size = input(Back.MAGENTA + Style.BRIGHT + "\nEnter the board size (minimum 4) and press Enter: ")
            print(Style.RESET_ALL)
            
            if size.isdigit():
                size = int(size)
                if size >= 4:
                    return size
            
            print(colored("\nInvalid board size. Please enter a number greater than or equal to 5.", "red", 'on_white'))


    def ship_numbers():
        pass

    def print_game_board(self, board, color, background):
        """
        Prints the game board.

        Args:
            board (list): The game board to print.
        """
        print(colored(' ' + ' '.join([str(i) for i in range(1, self.board_size + 1)]), color, background))
        for i, row in enumerate(board):
            print(colored(str(i + 1) + '|' + '|'.join(row) + '|', color, background))

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
                    print(colored("\nInvalid input or location already guessed. Please enter valid coordinates.", "red", "on_white"))
            except ValueError:
                print(colored("\nInvalid input. Please enter valid coordinates.", "red", "on_white"))


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
        else:
            print("\nA draw play")

    def is_game_over(self):
        """
        Checks if the game is over.

        Returns:
            bool: True if the game is over, False otherwise.
        """
        num_ships = self.board_size
        return self.player_score >= num_ships or self.computer_score >= num_ships

    def computer_guess(self):
        """
        Generates a computer guess for the ship location.

        Returns:
            tuple: The row and column indices of the computer's guess.
                   Returns None if all possible guesses have been made.
        """
        num_rows = len(self.Hidden_Pattern_Player)
        num_cols = len(self.Hidden_Pattern_Player[0])
        max_guesses = num_rows * num_cols

        if len(self.computer_guessed_locations) == max_guesses:
            return None

        while True:
            row = randint(0, num_rows - 1)
            col = randint(0, num_cols - 1)
            guess = (row, col)
            if guess not in self.computer_guessed_locations:
                self.computer_guessed_locations.append(guess)
                return guess

    def play(self):
        """
        Starts the Battleship game.
        """
        
        print(colored("\nLet's play Battleship!                     ", "black", "on_white"))
        print(colored("The '$' represents the hidden battleships. ", "black", "on_white"))
        print(colored("The '#' represents a hit.                  ", "black", "on_white"))
        print(colored("The '0' represents a miss.                 ", "black", "on_white"))
        print(colored("The 'x' represents a player's missed guess.", "black", "on_white"))
        print(colored("Good luck!                                 ", "black", "on_white"))

        self.board_size = self.get_board_size()
        self.Hidden_Pattern_Player = [['-']*self.board_size for _ in range(self.board_size)]
        self.Hidden_Pattern_Computer = [['-']*self.board_size for _ in range(self.board_size)]
        self.Guess_Pattern_Player = [['-']*self.board_size for _ in range(self.board_size)]
        self.Guess_Pattern_Computer = [['-']*self.board_size for _ in range(self.board_size)]

        self.create_ships(self.Hidden_Pattern_Player)
        self.create_ships(self.Hidden_Pattern_Computer)

        print(Back.WHITE + Style.NORMAL + "\nPlayer Board:" + Style.RESET_ALL)
        self.print_game_board(self.Guess_Pattern_Player, 'white', 'on_blue')


        print(Back.LIGHTCYAN_EX + Style.NORMAL + "\nComputer Board:")
        self.print_game_board(self.Guess_Pattern_Computer, 'white', 'on_green')

        while not self.is_game_over():
            valid_player_input = False
            valid_computer_input = False

            while not valid_player_input or not valid_computer_input:
                if not valid_player_input:
                    player_guess = self.get_unique_ship_location(self.player_guessed_locations)
                    if player_guess is None:
                        break

                    row, col = player_guess
                    if self.Hidden_Pattern_Computer[row][col] == '$':
                        print(colored("\nCongratulations! You hit a battleship!", "blue", "on_white"))
                        self.Guess_Pattern_Player[row][col] = '#'
                        self.player_score += 1
                    else:
                        print(colored("\nyou missed.", "blue", "on_white"))
                        self.Guess_Pattern_Player[row][col] = 'x'

                    print(colored("\nYou Guessed row: {} column: {}".format(row, col), "blue", "on_white"))
                    
                    
                    self.print_game_board(self.Guess_Pattern_Player, 'white', 'on_blue')
                    valid_player_input = True

                if not valid_computer_input:
                    computer_guess = self.computer_guess()
                    if computer_guess is None:
                        break

                    row, col = computer_guess
                    if self.Hidden_Pattern_Player[row][col] == '$':
                        print(colored("\nThe computer hit one of your battleships!", "red", "on_white"))
                        self.Hidden_Pattern_Player[row][col] = '#'
                        self.Guess_Pattern_Computer[row][col] = '#'
                        self.computer_score += 1
                    else:
                        print(colored("\nThe computer missed your battleship.", "red", "on_white"))
                        self.Hidden_Pattern_Player[row][col] = 'O'
                        self.Guess_Pattern_Computer[row][col] = 'O'
                    
                    print(colored("\nComputer Guessed row: {} column: {}".format(row, col), "red", "on_white"))
                    
                    self.print_game_board(self.Hidden_Pattern_Player, 'white', 'on_green')
                    self.print_score()
                    valid_computer_input = True

        if self.is_game_over():
            if self.player_score > self.computer_score:
                self.game_over_message('Player')
            elif self.player_score < self.computer_score:
                self.game_over_message('Computer')
            else:
                self.game_over_message('Draw')



    def game_home_page(self):
        """
        Displays the game home page and allows the user to choose to play or quit.
        """
        while True:
            print(colored("\nBattleship Game     ", "black", "on_yellow"))
            print(colored("Enter 1 to Play Game", "black", "on_yellow"))
            print(colored("Enter 2 to Quit     ", "black", "on_yellow"))
            
            choice = input(Back.MAGENTA + Style.NORMAL + "\nEnter your choice and press enter (1 or 2): ")
            print(Style.RESET_ALL)

            if choice == '1':
                self.__init__()  # Reset game state
                self.play()
            elif choice == '2':
                print("Goodbye!")
                break
            else:
                print(colored("\nInvalid choice. Please try again.", "red", "on_white"))




if __name__ == '__main__':
    game = BattleShipGame()
    game.game_home_page()