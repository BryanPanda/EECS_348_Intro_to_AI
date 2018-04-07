def opposite(side):
    if side == 'x': return 'o'
    if side == 'o': return 'x'
    raise ValueError, "invalid side: %s" % side

#------------------------------------------------------------------

class KonaneBoard:
    """

    This class implements a square Konane board of a given size.  The
    board state is represented as a two-dimensional list of 'x', 'o',
    and ' ' characters.  For example, KonaneBoard(8) constructs a board
    with 8 rows and 8 columns.  If b is a board and s is 'x' or 'o',

    b.possibleOpeningMoves(s) returns a list of board positions
    corresponding to the possible opening moves for side s, where
    each board position is represented as a (row, column) tuple.

    b.possibleNextMoves(s) returns a list of non-opening moves available
    for side s, where each move is a list of board positions of the form
    ((row1, column1), (row2, column2), ..., (rowN, columnN)).

    """

    def __init__(self, b):
        # Constructs a square Konane board of the specified size.
        self.size = len(b)
        self.state = b

    def __eq__(self, other):
        # Allows two KonaneBoard objects to be compared using the == operator.
        return self.state == other.state

    def __ne__(self, other):
        # Allows two KonaneBoard objects to be compared using the != operator.
        return self.state != other.state

    def __str__(self):
        # Returns a string representation of the board for printing.
        s = '\n     '
        for c in range(self.size):
            s += '%2d' % c
        s += '\n    +%s-+\n' % ('--' * self.size)
        for r in range(self.size):
            s += ' %2d | ' % r
            for c in range(self.size):
                if self.state[r][c] == ' ':
                    s += '. '
                elif self.state[r][c] in ('x', 'o'):
                    s += '%s ' % self.state[r][c]
                else:
                    s += '? '
            s += '|\n'
        s += '    +%s-+\n' % ('--' * self.size)
        return s

    def possibleOpeningMoves(self, side):
        # Returns a list of available board positions to use for the
        # opening move of side 'x' or 'o'.  Each board position is a
        # tuple of the form (row, column).
        m = self.size / 2
        n = self.size - 1
        if side == 'x' and self.size % 2 == 0:
            # even-sized board
            return [(0, 0), (m-1, m-1), (m, m), (n, n)]
        elif side == 'x' and self.size % 2 == 1:
            # odd-sized board
            return [(0, 0), (m, m), (n, n)]
        # side is 'o', so return positions adjacent to blank
        elif self.state[0][0] == ' ':
            return [(0, 1), (1, 0)]
        elif self.state[m-1][m-1] == ' ':
            return [(m-2, m-1), (m, m-1), (m-1, m-2), (m-1, m)]
        elif self.state[m][m] == ' ':
            return [(m-1, m), (m+1, m), (m, m-1), (m, m+1)]
        elif self.state[n][n] == ' ':
            return [(n-1, n), (n, n-1)]
        else:
            return []

    def possibleNextMoves(self, side):
        # Returns a list of the available non-opening moves for side 'x' or 'o'.
        # Each move is a list of two or more board positions, of the form
        #    ((row1, column1), (row2, column2), ..., (rowN, columnN))
        moves = []
        for (r, c) in self.allPositions():
            moves.extend(self.allMovesFrom(r, c, side))
        return moves

    def allPositions(self):
        # Returns a list of (row, column) positions for the entire board.
        return [(r, c) for r in range(self.size) for c in range(self.size)]

    def allMovesFrom(self, r, c, side):
        # Returns all available moves for side beginning at position (r, c).
        if self.state[r][c] == side:
            return self.linearMovesFrom(r, c, -2, 0, side) + \
                   self.linearMovesFrom(r, c, +2, 0, side) + \
                   self.linearMovesFrom(r, c, 0, +2, side) + \
                   self.linearMovesFrom(r, c, 0, -2, side)
        else:
            return []

    def linearMovesFrom(self, r, c, rDelta, cDelta, side):
        # Returns all available moves in a given direction beginning at
        # position (r, c) for side.  A direction is represented as a
        # pair of row and column offsets.
        r2, c2 = r + rDelta, c + cDelta
        if self.withinBounds(r2, c2) \
               and self.pieceBetween(r, c, r2, c2) == opposite(side) \
               and self.state[r2][c2] == ' ':
            rest = self.linearMovesFrom(r2, c2, rDelta, cDelta, side)
            return [((r, c), (r2, c2))] + [((r, c),) + m for m in rest]
        else:
            return []

    def withinBounds(self, r, c):
        # Returns True if position (r, c) is a valid board position.
        return 0 <= r < self.size and 0 <= c < self.size

    def pieceBetween(self, r1, c1, r2, c2):
        # Returns the board piece halfway between positions (r1, c1) and (r2, c2).
        return self.state[(r1 + r2) / 2][(c1 + c2) / 2]

    def posBetween(self, r1, c1, r2, c2):
        # Returns the board piece halfway between positions (r1, c1) and (r2, c2).
        return [(r1 + r2) / 2,(c1 + c2) / 2]

    def firstMove(self, s, r, c):
        # makes a first move
        self.state[r][c] = ' '
        
    def nextMove(self, s, move):
        for frm, to in zip(move, move[1:]):
            self._makeJump(s, frm, to)
    
    def _makeJump(self, s, frm, to):
        self.state[frm[0]][frm[1]] = ' '
        self.state[to[0]][to[1]] = s
        remove = self.posBetween(frm[0], frm[1], to[0], to[1])
        self.state[remove[0]][remove[1]] = ' '