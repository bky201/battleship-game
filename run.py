from random import randint
from colorama import Back, Style
from colorama import init
from termcolor import colored
import pyfiglet

init()


class BattleShipGame:
    def __init__(self):
        self.size = 0
        self.player_score = 0
        self.com_score = 0
        self.Hidden_Bord = []
        self.Hidden_Pattern_Comp = []
        self.Player_Bord = []
        self.Guess_Pattern_Comp = []
        self.player_guessed_locations = []
        self.computer_guessed_locations = []

    def get_size(self):
        """
        Prompts the user to enter the board size and validates the input.

        Returns:
            int: The validated board size.
        """
        while True:
            print(Back.MAGENTA+"Enter board size + Enter key:"+Style.RESET_ALL)
            size = input(Back.MAGENTA+"Enter board size >=4:"+Style.RESET_ALL)
            if size.isdigit():
                size = int(size)
                if size >= 4:
                    return size
            print(colored("Invalid board size.", "red", 'on_white'))
            print("\n")

    def print_board(self, board, clr, bkgrnd):
        """
        Prints the game board.

        Args:
            board (list): The game board to print.
        """
        print(' ' + ' '.join([str(i) for i in range(1, self.size + 1)]) + '  ')
        for i, row in enumerate(board):
            print(colored(str(i + 1) + '|' + '|'.join(row) + '|', clr, bkgrnd))

    def is_valid_input(self, value):
        """
        Checks if the input value is valid.

        Args:
            value (str): The input value to check.

        Returns:
            bool: True if the input value is valid, False otherwise.
        """
        return value in [str(i) for i in range(1, self.size + 1)]

    def uniq_loc(self, guessed_locations):
        """
        Gets a unique ship location from the user.
        Args:
            guessed_locations (list): The list of already guessed locations.
        Returns:
            tuple: The row and column indices of the ship location.
                    Returns None if all possible guesses have been made.
        """
        rows = len(self.Hidden_Bord)
        cols = len(self.Hidden_Bord[0])
        max_guesses = rows * cols

        num_guesses = len(guessed_locations)
        if num_guesses >= max_guesses:
            print("You have made all possible guesses. The game is over.")
            return None

        while True:
            try:
                print('Enter a ship row and column separated by "+"(r+c)')
                row, column = input(f'row 1-{rows} col 1-{cols}: ').split('+')
                row = int(row)
                column = int(column)

                if (
                    1 <= row <= rows
                    and 1 <= column <= cols
                    and (row - 1, column - 1) not in guessed_locations
                    and self.is_valid_input(str(row))
                    and self.is_valid_input(str(column))
                ):
                    return row - 1, column - 1
                elif (
                    1 <= row <= rows
                    and 1 <= column <= cols
                    and (row - 1, column - 1) in guessed_locations
                    and self.is_valid_input(str(row))
                    and self.is_valid_input(str(column))
                ):
                    return None
                else:
                    print(colored("Invalid location.", "red", "on_white"))
                    print("\n")
            except ValueError:
                print(colored("Invalid input. ", "red", "on_white"))
                print("\n")

    def create_ships(self, board):
        """
        Randomly creates ships on the game board.

        Args:
            board (list): The game board to create ships on.
        """
        nums = self.size

        ship_locations = set()
        for i in range(nums):
            while True:
                # Generate random ship location
                ship_r = randint(0, self.size - 1)
                ship_c = randint(0, self.size - 1)
                ship_location = (ship_r, ship_c)
                if ship_location not in ship_locations:
                    ship_locations.add(ship_location)
                    # Place ship on the board
                    board[ship_r][ship_c] = "$"
                    break

    def print_score(self):
        """
        Prints the current scores of the players.
        """
        print(colored(" Player Score  : {} ".format(self.player_score), "red"))
        print(colored(" Computer Score: {} ".format(self.com_score), "red"))

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
            print("\n")
            game_over = pyfiglet.figlet_format("Great You win!", font="bubble")
            print(game_over)
        elif result == 'Computer':
            print("\n")
            game_over = pyfiglet.figlet_format("Computer wins!", font="bubble")
            print(game_over)
        else:
            print("\n")
            game_over = pyfiglet.figlet_format(" A draw play ", font="bubble")
            print(game_over)

    def is_game_over(self):
        """
        Checks if the game is over.

        Returns:
            bool: True if the game is over, False otherwise.
        """
        nums = self.size
        return self.player_score >= nums or self.com_score >= nums

    def computer_guess(self):
        """
        Generates a computer guess for the ship location.

        Returns:
            tuple: The row and column indices of the computer's guess.
                   Returns None if all possible guesses have been made.
        """
        rows = len(self.Hidden_Bord)
        cols = len(self.Hidden_Bord[0])
        max_guesses = rows * cols

        if len(self.computer_guessed_locations) == max_guesses:
            return None

        while True:
            (row, col) = (randint(0, rows - 1), randint(0, rows - 1))
            guess = (row, col)
            if guess not in self.computer_guessed_locations:
                self.computer_guessed_locations.append(guess)
                return guess

    def play(self):
        """
        Starts the Battleship game.
        """
        print("\n")
        print(colored("Let's play Battleship!      ", "black", "on_white"))
        print(colored("The '$'-hidden battleships. ", "black", "on_white"))
        print(colored("The '#' represents a hit.   ", "black", "on_white"))
        print(colored("The '0' represents a miss.  ", "black", "on_white"))
        print(colored("The 'x' a player's missed.  ", "black", "on_white"))
        print(colored("Good luck!                  ", "black", "on_white"))
        print("\n")

        self.size = self.get_size()
        self.Hidden_Bord = [['-']*self.size for _ in range(self.size)]
        self.Hidden_Pattern_Comp = [['-']*self.size for _ in range(self.size)]
        self.Player_Bord = [['-']*self.size for _ in range(self.size)]
        self.Guess_Pattern_Comp = [['-']*self.size for _ in range(self.size)]

        self.create_ships(self.Hidden_Bord)
        self.create_ships(self.Hidden_Pattern_Comp)

        print("\n")
        print(colored("Player Board:", "black", "on_white"))
        self.print_board(self.Player_Bord, 'white', 'on_blue')
        print("\n")

        print(colored("Computer Board:", "black", "on_white"))
        self.print_board(self.Guess_Pattern_Comp, 'white', 'on_magenta')
        print("\n")

        while not self.is_game_over():
            valid_player_input = False
            valid_computer_input = False

            while not valid_player_input or not valid_computer_input:
                if not valid_player_input:
                    player_guess = self.uniq_loc(self.player_guessed_locations)
                    self.player_guessed_locations.append(player_guess)
                    if player_guess is None:
                        print("\n")
                        print(colored(">> Already Guessed", "red", "on_white"))
                        print(colored(">> Try again      ", "red", "on_white"))
                        print("\n")
                        break

                    row, col = player_guess
                    print("\n")
                    if self.Hidden_Pattern_Comp[row][col] == '$':
                        print(colored("You hit one!", "blue", "on_white"))
                        self.Player_Bord[row][col] = '#'
                        self.player_score += 1
                    else:
                        print(colored("you missed.-", "blue", "on_white"))
                        self.Player_Bord[row][col] = 'x'

                    print(colored("Your Guessed", "blue", "on_white"))
                    print(colored("row: {}  ".format(row), "blue", "on_white"))
                    print(colored("col: {}  ".format(col), "blue", "on_white"))
                    self.print_board(self.Player_Bord, 'white', 'on_blue')
                    valid_player_input = True

                if not valid_computer_input:
                    computer_guess = self.computer_guess()
                    if computer_guess is None:
                        break

                    row, col = computer_guess
                    print("\n")
                    if self.Hidden_Bord[row][col] == '$':
                        print(colored("computer hits ship", "red", "on_white"))
                        self.Hidden_Bord[row][col] = '#'
                        self.Guess_Pattern_Comp[row][col] = '#'
                        self.com_score += 1
                    else:
                        print(colored("computer missed.  ", "red", "on_white"))
                        self.Hidden_Bord[row][col] = 'O'
                        self.Guess_Pattern_Comp[row][col] = 'O'
                    print(colored("Computer Guessed  ", "red", "on_white"))
                    print(colored("row: {}   ".format(row), "red", "on_white"))
                    print(colored("col: {}   ".format(col), "red", "on_white"))
                    self.print_board(self.Hidden_Bord, 'white', 'on_magenta')
                    print("\n")
                    self.print_score()
                    print("\n")
                    valid_computer_input = True

        if self.is_game_over():
            if self.player_score > self.com_score:
                self.game_over_message('Player')
            elif self.player_score < self.com_score:
                self.game_over_message('Computer')
            else:
                self.game_over_message('Draw')

    def game_home_page(self):
        """
        Displays the home page and allows the user to choose to play or quit.
        """
        while True:
            print("\n")
            battle = pyfiglet.figlet_format("Battleship", font="bulbhead")
            print(battle)
            game = pyfiglet.figlet_format("***** Game *****", font="bulbhead")
            print(game)
            print("\n")
            print(colored("Enter 1 + Enter Key to Play", "black", "on_yellow"))
            print(colored("Enter 2 + Enter Key to Quit", "black", "on_yellow"))
            print("\n")
            choice = input(Back.MAGENTA+"Enter (1 or 2):"+Style.RESET_ALL)
            if choice == '1':
                self.__init__()  # Reset game state
                self.play()
            elif choice == '2':
                game = pyfiglet.figlet_format("Goodbye!", font="bulbhead")
                print(game)
                break
            else:
                print(colored("\nInvalid input try again.", "red", "on_white"))


if __name__ == '__main__':
    game = BattleShipGame()
    game.game_home_page()
