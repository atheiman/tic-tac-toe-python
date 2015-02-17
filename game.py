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
        raw = raw_input(
            "Which square do you choose? (row,col) (Ex: \"1,2\") "
        ).strip()
        try:
            row = int(raw.split(',')[0]) - 1
            col = int(raw.split(',')[1]) - 1
        except ValueError as e:
            raise SystemExit(
                "row and col should be integers.\n"
                "Way to go {t}'s, you ruin all the fun.".format(t=self.turn,
                                                                e=e,)
            )
        except IndexError as e:
            raise SystemExit(
                "Need both a row and a column.\n"
                "Way to go {t}'s, you ruin all the fun.".format(t=self.turn,
                                                                e=e,)
            )
        try:
            if not self.rows[row][col].strip():
                return (row, col)
            else:
                raise SystemExit(
                    "row {r}, col {c} is already occupied.\n"
                    "Way to go {t}'s, you ruin all the fun.".format(
                        r=row,
                        c=col,
                        t=self.turn,
                    )
                )
        except IndexError as e:
            raise SystemExit(
                "maximum row and col value is 3.\n"
                "Way to go {t}'s, you ruin all the fun.".format(t=self.turn,
                                                                e=e)
            )


    def turn_cycle(self):
        print "You're up, {turn}'s".format(turn=self.turn)
        row, col = self.get_input()
        self.rows[row][col] = self.turn
        self.draw()
        self.check_winner()
        if self.turn == 'X': self.turn = 'O'
        else: self.turn = 'X'


    def check_winner(self):
        """Set self.winner to True when someone has won the game.
        """
        winning_sets = [
            ((0,0), (0,1), (0,2)),
            ((1,0), (1,1), (1,2)),
            ((2,0), (2,1), (2,2)),
            ((0,0), (1,0), (2,0)),
            ((0,1), (1,1), (2,1)),
            ((0,2), (1,2), (2,2)),
            ((0,0), (1,1), (2,2)),
            ((0,2), (1,1), (2,0)),
        ]
        for s in winning_sets:
            spaces = []
            for space in s:
                row = space[0]
                col = space[1]
                spaces.append(self.rows[row][col])
            if spaces[0] == spaces[1] == spaces[2] and spaces[0] != ' ':
                self.winner = spaces[0]


if __name__ == "__main__":
    board = Board()
    board.draw()
    while not board.winner:
        board.turn_cycle()
    print '\n***\nWe have a winner! {w}\n***'.format(w=board.winner)
