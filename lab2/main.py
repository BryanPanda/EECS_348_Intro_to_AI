import copy
import random
import konane as kb
import student_code as student

# sample boards used for evaluation of student implementations

boardA = [[' ',' ','x','o'],
          ['o','x','o','x'],
          ['x','o','x','o'],
          ['o','x','o','x']]

boardB = [['x','o','x','o'],
          ['o',' ',' ','x'],
          ['x','o','x','o'],
          ['o','x','o','x']]

boardC = [['x','o','x','o','x','o'],
          ['o','x','o','x','o','x'],
          ['x','o','x','o','x','o'],
          ['o','x',' ',' ','o','x'],
          ['x','o','x','o','x','o'],
          ['o','x','o','x','o','x']]

# 'gold' sequences of moves that students' implementations must match

ans1 = [((0, 3), (0, 1)), ((2, 3), (0, 3)), ((2, 1), (2, 3))]

ans2 = [((3, 5), (3, 3)), ((4, 2), (2, 2)),
        ((1, 3), (1, 1)), ((3, 3), (1, 3)),
        ((4, 4), (2, 4)), ((5, 5), (3, 5)),
        ((4, 0), (4, 2)), ((2, 0), (4, 0)),
        ((5, 3), (5, 5)), ((4, 2), (4, 4)),
        ((0, 4), (0, 2)), ((4, 0), (4, 2)),
        ((5, 1), (5, 3)), ((4, 2), (4, 4))]

ans3 = [((3, 5), (3, 3)), ((4, 2), (2, 2)),
        ((1, 3), (1, 1)), ((3, 3), (1, 3)),
        ((4, 4), (2, 4)), ((5, 5), (3, 5)),
        ((4, 0), (4, 2)), ((2, 0), (4, 0)),
        ((5, 3), (5, 5)), ((4, 2), (4, 4)),
        ((0, 4), (0, 2)), ((4, 0), (4, 2)),
        ((5, 1), (5, 3)), ((4, 2), (4, 4))]

ans4 = [((3, 5), (3, 3)), ((4, 2), (2, 2)),
        ((1, 3), (1, 1)), ((3, 3), (1, 3)),
        ((5, 5), (3, 5)), ((4, 0), (4, 2)),
        ((2, 0), (4, 0)), ((3, 1), (1, 1)),
        ((0, 4), (0, 2)), ((4, 4), (2, 4)),
        ((5, 3), (5, 5)), ((5, 1), (5, 3)),
        ((4, 0), (4, 2))]

# specification of boards, gold sequences and game parameters used to test student code
game1 = [copy.deepcopy(boardA),ans1,100,5,'First Move','MiniMax','o']
game2 = [copy.deepcopy(boardC),ans2,100,5,'First Move','MiniMax','x']
game3 = [copy.deepcopy(boardC),ans3,100,5,'First Move','AlphaBeta','x']
game4 = [copy.deepcopy(boardC),ans4,100,7,'First Move','AlphaBeta','x']

games = [game1,game2,game3,game4]

verbose = False # flag to control level of debugging output

# function used to test student implementation for an individual game
def test(board,max_moves,depth,algoG,algoS,student_xo):
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
            print('  Game %d: PASSED' % i)
        else:
            print('  Game %d: FAILED' % i)

if __name__ == "__main__":
    main()
    
