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

    def validate_input():
        pass

    def guess_ship_location():
        pass

    def create_battle_ships():
        pass

    def count_hits():
        pass

    def game_over_message():
        pass

    def is_game_over():
        pass

    def play():
        pass

    def computer_guess():
        pass

    def play():
        pass


    def game_home_page(self):
        pass


if __name__ == '__main__':
    game = BattleShipGame()
    game.game_home_page()