class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'

    def print_board(self):
        print('-------------')
        for i in range(0, 9, 3):
            print(f'| {self.board[i]} | {self.board[i+1]} | {self.board[i+2]} |')
            print('-------------')

    def make_move(self, position):
        self.board[position] = self.current_player

    def switch_player(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'

    def is_winner(self):
        winning_positions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
            (0, 4, 8), (2, 4, 6)  # diagonals
        ]
        for position in winning_positions:
            if self.board[position[0]] == self.board[position[1]] == self.board[position[2]] != ' ':
                return True
        return False

    def is_board_full(self):
        return ' ' not in self.board

    def play(self):
        while True:
            self.print_board()
            position = int(input(f"{self.current_player}'s turn. Enter a position (1-9): ")) - 1
            if self.board[position] == ' ':
                self.make_move(position)
                if self.is_winner():
                    self.print_board()
                    print(f'{self.current_player} wins!')
                    break
                elif self.is_board_full():
                    self.print_board()
                    print('Tie game!')
                    break
                else:
                    self.switch_player()
            else:
                print('That position is already taken. Try again.')