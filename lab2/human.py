import copy
import konane as kb
import student

# This is the board used for a human game
# Either change this board or make a new board
# and pass it in to the function call at the
# bottom of this file
boardA = [[' ',' ','x','o'],
          ['o','x','o','x'],
          ['x','o','x','o'],
          ['o','x','o','x']]

def humanVsAI(human,ai_algorithm,board):
    b = kb.KonaneBoard(board)

    if human == 'x':
        player_x = student.player(b,'x',99,"Human")
        player_o = student.player(b,'o',99,ai_algorithm)
    else:
        player_o = student.player(b,'o',99,"Human")
        player_x = student.player(b,'x',99,ai_algorithm)

    print('Konane Test Game')
    print('  AI Algorithm:  %s' % ai_algorithm)
    print('  Human Playing as: %s' % human)
    print('  Starting Board:')
    print(b)
    
    moves_o = []
    moves_x = []

    done = False
    while not done and len(moves_o) <= 99:
        [done,move] = player_x.takeTurn()
        moves_x.append(move)
        if done:
            print('PlayerO WINS!!!')
        else:
            print(b)
            [done,move] = player_o.takeTurn()
            moves_o.append(move)
            if done:
                print('PlayerX WINS!!!')
            else:
                print(b)

    print('Game Over.')

if __name__ == "__main__":
    # to play a game as o, with a different algorithm
    # or on a different board adjust the parameters here
	humanVsAI('x', "Random", boardA) # play as x against random on boardA
