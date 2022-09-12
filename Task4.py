# task 4 of Abostack game, runs through the game and uses classes of 1,2,3
# Author: Saumya Rada 1709193

from Abostack import BStack
from Abostack import Card
from Abostack import Abostack

playing = True
while playing:
    # To start the game a player has to choose the size of the AbacoStack 
    # by selecting the number of stacks between 2 and 5 and selecting the depth of the stacks between 2 and 4. 
    stack_nom = int(input('Enter the number of stacks in your game (between 2 to 5):'))
    stack_depth = int(input('Enter the depth of the stacks (between 2 to 4):'))
    
    # the program should iteratively generate a new random configuration card and allow the user to solve the puzzle
    print('This is your card:')
    card = Card(stack_nom,stack_depth)
    card.show()
    abostack = Abostack(stack_nom,stack_depth)
    
    current_game = True
    while current_game:
        # prompt user to either play one move, a sequence of moves (max 5 at a time), reset the state game to retry the same card, or quit
        move = input('Enter your move(s) [Q for quit and R to reset]:')
        move = move.rstrip()
        if move.upper() == 'Q':
            playing = False # quits game
        elif move.upper() == 'R':
            abostack.reset() # resets current card
        else:
            moves = move.split(' ')
            moves = moves[:5]
            moves_done = 0
            for move in moves:
                if abostack.check_invalid(move):
                    abostack.moveBead(move)  # carries out move
                    moves_done += 1
                else:
                    moves = moves[:moves_done]
            
        abostack.show() # displays state of game
        print('Number of moves: %i' % (abostack.return_moves()))
        
        if abostack.isSolved(card):
            print('Congratulations, you have solved the puzzle in %i moves!' % (total_moves))
            reply = input('Attempt another card?(Y/N)')
            if reply.upper() == 'N':
                playing = False
            else:
                current_game = False
                
        
        
        
        
        
        
        
        
    