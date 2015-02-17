import random


class Board(object):
    def __init__(self, x=3, y=3):
        if x < 1 or y < 1:
            raise Exception('Board needs x and y.')
        self.rows = []
        for i in range(0, y):
            row = []
            for i in range(0, x):
                row.append(' ')
            self.rows.append(row)
        # Set the turn randomly
        if bool(random.getrandbits(1)):
            self.turn = 'X'
        else:
            self.turn = 'O'


    winner = False


    def get_row_string(self, row_index):
        return_str = '| '
        for c in range(0, len(self.rows[row_index])):
            return_str += '{col} | '.format(col=self.rows[row_index][c])
        return return_str


    def draw(self):
        output = '+---+---+---+\n'
        for r in range(0, len(self.rows)):
            output += self.get_row_string(r)
            output += '\n+---+---+---+\n'
        print output


    def get_input(self):
        """Return a tuple of (row, col)
        """
        raw = raw_input("Which square do you choose? (row,col) (Ex: \"1, 2\") ").strip()
        row = int(raw.split(',')[0]) - 1
        col = int(raw.split(',')[1]) - 1
        if not self.rows[row][col].strip():
            return (row, col)
        else:
            raise Exception('{},{} is already occupied'.format(row, col))


    def turn_cycle(self):
        print "\nYou're up, {turn}'s".format(turn=self.turn)
        row, col = self.get_input()
        self.rows[row][col] = self.turn
        self.draw()
        self.check_winner()
        if self.turn == 'X': self.turn = 'O'
        else: self.turn = 'X'


    def check_winner(self):
        """Set self.winner to True when someone has won the game.
        """
        pass


if __name__ == "__main__":
    board = Board()
    while not board.winner:
        board.turn_cycle()
