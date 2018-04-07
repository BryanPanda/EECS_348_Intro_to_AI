import copy
import random
import konane as kb
import student_code as student
import time

#timing used for grading:   game1:1,
#                           game2:1,
#                           game3:1,
#                           game4:2,
#                           game5:45,
#                           game6:3,
#                           game7:1,
#                           game8:2,
#                           game9:4 and
#                           game10:173

# sample boards used for evaluation of student implementations
boardA = [[' ',' ',' ',' '],
          [' ',' ',' ',' '],
          [' ','x',' ',' '],
          ['o','o','o',' ']]

boardB = [['x','o','x','o'],
          ['o',' ',' ','x'],
          ['x','o','x','o'],
          ['o','x','o','x']]

boardC = [['x',' ','x',' ',' ','o'],
          [' ',' ',' ',' ',' ','x'],
          [' ','o',' ',' ',' ','o'],
          [' ','x',' ',' ','o','x'],
          ['x',' ','x','o','x',' '],
          ['o','x','o','x','o',' ']]

boardD = [['x','o','x','o','x','o'],
          ['o','x','o','x','o','x'],
          ['x','o','x','o','x','o'],
          ['o','x',' ',' ','o','x'],
          ['x','o','x','o','x','o'],
          ['o','x','o','x','o','x']]

boardE = [['x','o','x','o','x','o'],
          ['o','x','o','x','o','x'],
          ['x','x','x','o','x','o'],
          ['o','x',' ',' ','o','x'],
          ['x','o','x','x','x','o'],
          ['o','x','o','o','o','x']]

boardF = [['x','o','x','o','x','o','x','o','x'],
          ['o','x','o','x','o','x','o','x','o'],
          ['x','o','x','o','x','o','x','o','x'],
          ['o','x','o','x','o','x','o','x','o'],
          ['x','o','x','o','x','o','x','o','x'],
          ['o','x','o','x','o','x','o','x','o'],
          ['x','o','x','o','x','o','x','o','x'],
          ['o','x','o','x','o','x','o','x',' '],
          ['x','o','x','o','x','o','x','o',' ']]

# 'gold' sequences of moves that students' implementations must match
ans1 = [None]

ans2 = [((3, 1), (1, 1)), ((3, 3), (3, 1)),
        ((1, 3), (3, 3)), ((0, 0), (0, 2)),
        ((2, 0), (0, 0))]

ans3 = [((0, 1), (2, 1)), ((3, 0), (3, 2)),
        ((2, 1), (2, 3)), ((1, 0), (3, 0))]

ans4 = [((3, 1), (1, 1)), ((4, 4), (2, 4)),
        ((5, 3), (5, 5)), ((5, 1), (5, 3)),
        ((4, 0), (4, 2))]

ans5 = [((3, 5), (3, 3)), ((4, 2), (2, 2)),
        ((1, 3), (1, 1))]

ans6 = [((4, 3), (2, 3)), ((1, 4), (1, 2)),
        ((0, 1), (2, 1)), ((0, 3), (0, 1)),
        ((0, 5), (0, 3)), ((2, 5), (0, 5)),
        ((2, 3), (2, 5)), ((4, 1), (4, 3)),
        ((4, 3), (2, 3)), ((2, 3), (2, 1)),
        ((5, 4), (3, 4)), ((5, 2), (5, 4))]

ans7 = [((1, 3), (3, 3)), ((1, 5), (1, 3)),
        ((2, 4), (2, 2))]

ans8 = [((1, 2), (3, 2)), ((2, 5), (2, 3)),
        ((3, 0), (3, 2)), ((5, 2), (3, 2)),
        ((5, 3), (3, 3)), ((4, 5), (4, 3), (4, 1)),
        ((1, 0), (3, 0))]

ans9 = [((8, 6), (8, 8)), ((6, 6), (6, 8)),
        ((4, 6), (4, 8)), ((6, 4), (6, 6)),
        ((2, 6), (2, 8)), ((3, 5), (1, 5)),
        ((2, 4), (2, 6)), ((0, 6), (0, 4)),
        ((2, 2), (0, 2)), ((4, 2), (2, 2)),
        ((3, 1), (1, 1)), ((8, 4), (8, 6)),
        ((8, 2), (8, 4)), ((5, 5), (3, 5)),
        ((0, 8), (0, 6), (0, 4)), ((2, 8), (0, 8)),
        ((2, 6), (0, 6)), ((5, 1), (3, 1)),
        ((4, 8), (2, 8)), ((4, 4), (2, 4)),
        ((3, 5), (1, 5)), ((7, 1), (5, 1), (3, 1)),
        ((0, 8), (2, 8)), ((3, 1), (3, 3)),
        ((6, 2), (4, 2))]
        
ans10 = [((8, 6), (8, 8)), ((6, 6), (6, 8)),
         ((4, 6), (4, 8)), ((6, 4), (6, 6)),
         ((2, 6), (2, 8)), ((8, 4), (8, 6)),
         ((4, 4), (4, 6)), ((2, 4), (2, 6)),
         ((3, 1), (1, 1)), ((3, 3), (1, 3)),
         ((2, 2), (2, 4)), ((0, 2), (0, 4)),
         ((0, 4), (0, 6)), ((5, 1), (3, 1)),
         ((4, 2), (2, 2)), ((5, 3), (3, 3)),
         ((7, 1), (5, 1)), ((3, 3), (3, 1)),
         ((6, 2), (6, 0)), ((7, 3), (5, 3))]

# specification of boards, gold sequences and game parameters used to test student code
game1 = [copy.deepcopy(boardA),ans1,100,5,'First Move','MiniMax','x']
game2 = [copy.deepcopy(boardB),ans2,100,5,'First Move','MiniMax','x']
game3 = [copy.deepcopy(boardB),ans3,100,7,'First Move','AlphaBeta','o']
game4 = [copy.deepcopy(boardC),ans4,100,7,'First Move','AlphaBeta','x']
game5 = [copy.deepcopy(boardD),ans5,3,7,'First Move','AlphaBeta','x']
game6 = [copy.deepcopy(boardD),ans6,100,4,'First Move','AlphaBeta','o']
game7 = [copy.deepcopy(boardE),ans7,3,4,'First Move','MiniMax','x']
game8 = [copy.deepcopy(boardE),ans8,100,4,'First Move','MiniMax','o']
game9 = [copy.deepcopy(boardF),ans9,100,2,'First Move','MiniMax','x']
game10 = [copy.deepcopy(boardF),ans10,100,5,'First Move','AlphaBeta','x']

# list of game for evaluation
games = [game1,game2,game3,game4,game5,game6,game7,game8,game9,game10]

verbose = False # flag to control level of debugging output

# function used to test student implementation for an individual game
def test(board,max_moves,depth,algoG,algoS,student_xo):
    start = time.clock()
    moves_x = []
    moves_o = []
    
    b = kb.KonaneBoard(board)

    # instantiates student and grader players based upon students' 'x' or 'o' designation
    if student_xo == 'x':
        player_x = student.player(b,'x',depth,algoS)
        player_o = student.player(b,'o',depth,algoG)
    else:
        player_o = student.player(b,'o',depth,algoS)
        player_x = student.player(b,'x',depth,algoG)

    # displays paramters of specific game used for evaluation
    if verbose:
        print('Konane Test Game')
        print('  Grader Algorithm:   %s' % algoG)
        print('  Student Algorithm:  %s' % algoS)
        print('  Student Playing as: %s' % student_xo)
        print('  Maximum Moves:      %d' % max_moves)
        print('  Maximum Depth:      %d' % depth)
        print('  Boards:')
        print(b)

    # players continue to alternate turns until gameover or maximum moves reached
    done = False
    while not done and len(moves_o) < max_moves:
        [done,move] = player_x.takeTurn()
        moves_x.append(move)
        if done:
            if verbose:
                print 'PlayerX moved', move
                print(b)
                print('PlayerO WINS!!!')
        else:
            if verbose:
                print 'PlayerX moved', move
                print(b)
            [done,move] = player_o.takeTurn()
            moves_o.append(move)
            if done:
                if verbose:
                    print 'PlayerO moved', move
                    print(b)
                    print('PlayerX WINS!!!')
            else:
                if verbose:
                    print 'PlayerO moved', move
                    print(b)
                    
    if verbose:
        print('Game Over.')

    print "Timing:", (time.clock()-start)
    # returns appropriate list of moves based upon player's 'x' or 'o' designation
    if student_xo == 'x':
        return(moves_x)
    else:
        return(moves_o)
            
def main():
    print('Starting Konane tests...\n')

    # loop through all individual games and compare student moves with gold moves
    for i in range(len(games)):
        board =     games[i][0][:]
        gold =      games[i][1]
        max_moves = games[i][2]
        depth =     games[i][3]
        algoS =     games[i][4]
        algoG =     games[i][5]
        xo =        games[i][6]

        ans = test(board,max_moves,depth,algoS,algoG,xo)

        if verbose:
            print(ans)
        if ans == gold:
            print('  Game %d: PASSED' % (i+1))
        else:
            print('  Game %d: FAILED' % (i+1))

if __name__ == "__main__":
    main()
