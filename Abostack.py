# task 1,2,3 classes of Abostack game
# Author: Saumya Rada 1709193
import random

class Card():
    # class named Card representing a configuration card. 
    # An instance of this class should have one private property, beads a list storing in order the beads in each stack
    # reset() to reshuffle the card to generate a new configuration, show() to display a card, and 
    # stack(number) to return the ordered list of elements top to bottom in the number stack    
    def __init__(self, nom_stacks, depth_stacks):
        self.size = nom_stacks * depth_stacks
        self.nom_stacks = nom_stacks
        self.depth_stacks = depth_stacks
        self.beads = []
        colours = ['A','B','C','D','E','F']
        stack_filled = 0
        for stack in range(self.nom_stacks):
            for bead in range(self.depth_stacks):
                self.beads.append(colours[stack_filled])
            stack_filled += 1
        random.shuffle(self.beads)
        
    def return_stacks_split(self):
        '''split self.beads into lists of elements representing the stacks
        Inputs: None
        Returns: stacks_split(list) - contains list of lists of elements in each stack'''
        stacks_split = []
        bead_added = 0
        for stack in range(self.nom_stacks):
            stack = []
            for bead in range(self.depth_stacks):
                stack.append(self.beads[bead_added])
                bead_added += 1
            stacks_split.append(stack)
        return stacks_split    
        
    def reset(self):
        random.shuffle(self.beads)
        
    def show(self):
        '''represents all the stacks in the card in the form of the card configuration
        Inputs: None
        Returns: None
        '''
        # split self.beads into lists of stacks
        stacks_split = []
        bead_added = 0
        for stack in range(self.nom_stacks):
            stack = []
            for bead in range(self.depth_stacks):
                stack.append(self.beads[bead_added])
                bead_added += 1
            stacks_split.append(stack)
            
        # print card
        pos = 0
        for stack in range(self.depth_stacks):
            crnt_stack = 0
            print('| ', end= '')
            for bead in range(self.nom_stacks):
                print(stacks_split[crnt_stack][pos], end = ' ')
                crnt_stack += 1
            print('|')
            pos += 1

            
    def stack(self,number):
        '''returns a list of elements of the stack given by number
        Inputs: number(int) - specifies stack
        Returns: stack(list) - list of elements of stack
        '''
        start_index = (number - 1) * self.depth_stacks 
        end_index = start_index + self.depth_stacks 
        stack = []
        for bead in range(start_index, end_index):
            stack.append(self.beads[bead])
        return stack
    
    def replace(self,filename, n):
        '''reads from the file filename  the nth config card and replaces the card state with the new configuration
        Inputs: filename (str) - name of file to be modified
                n (int) - line of file to be modified
        Returns: None
        '''
        self.reset()
        card_line = ' '.join(self.beads)
        file_mode = 'r'
        infile = open(filename, file_mode)
        all_lines = infile.read()
        all_lines_list = all_lines.splitlines()   
        infile.close()
        with open(filename,'w') as f:
            for i in range(n):
                f.write(all_lines_list[i] + '\n')
            f.write(card_line + '\n')
            for i in range(n+1,len(all_lines_list)):
                f.write(all_lines_list[i] + '\n')
                
        
class BStack: 
    # task 2 - Implement a Bounded Stack with isFull() method
    def __init__(self, capacity):
        assert isinstance(capacity, int), ('Error: Type error: %s' % (type(capacity)))
        assert capacity > 0, ('Error: Illegal capacity: %d' % (capacity)) 
        
        self.items = []
        self.capacity = capacity
        self.accesses = 0
        
    def push(self, item):
        '''adds item to top of stack
        Inputs: item (any object) - added
        Returns: None
        '''
        if len(self.items) >= self.capacity:
            raise Exception('Error: Queue is full')
        self.items.append(item)
    
    # MODIFY: RAISE AN EXCEPTION IF THIS METHOD IS INVOKED ON AN EMPTY STACK
    def pop(self): 
        '''removes and returns item from the top of the stack
        Inputs: None
        Returns: item removed
        '''
        if len(self.items) <= 0:
            raise Exception('Error: Queue is empty')
        return self.items.pop() 
    
    # MODIFY: RAISE AN EXCEPTION IF THIS METHOD IS INVOKED ON AN EMPTY STACK
    def peek(self):
        '''returns item at the top of the stack without removing it
        Inputs: None
        Returns: item at the top of the stack
        '''
        if len(self.items) <= 0:
            raise Exception('Error: Queue is empty')        
        return self.items[len(self.items)-1]
    
    def checkEmpty(self):
        '''checks if stack is empty for abostack game (empty if list only has '.' element)
        Inputs: None
        Returns: None
        '''
        return self.items == ['.']*self.capacity
    
    def checkFull(self):
        '''checks if stack is full for abostack game (full if no '.' element)
        Inputs: None
        Returns: None
        '''
        return ('.' not in self.items)
    
    def moveColorUp(self):
        '''moves color up the stack for abostack game
        Inputs: None
        Returns: None
        '''
        i = 0
        while self.items[i+1] != '.':
            i += 1
        self.items[i+1] = self.items[i]
        self.items[i] = '.'
        
    def moveColorDown(self):
        '''moves color down the stack for abostack game
        Inputs: None
        Returns: None
        '''        
        i = 0
        while not (self.items[i] == '.' and self.items[i+1] != '.'):
            i += 1
        self.items[i] = self.items[i+1]
        self.items[i+1] = '.'
        
    def return_for_display(self):
        '''returns item for display for abostack game in correct order
        Inputs: None
        Returns: item 
        '''
        if self.accesses == self.capacity:
            self.accesses = 1
        else:
            self.accesses += 1
        return self.items[len(self.items)-self.accesses]
    
    def return_items_for_show(self):
        '''returns list of items in stack for show
        Inputs: None
        Returns: None
        '''
        return self.items
    
    def isEmpty(self):
        '''checks if stack is empty
        Inputs: None
        Returns: None
        '''
        return self.items == []
    
    def isFull(self):
        '''checks if stack is full
        Inputs: None
        Returns: None
        '''
        return len(self.items) == self.capacity
    
    def size(self):
        '''returns size of list
        Inputs: None
        Returns: None
        '''
        return len(self.items)
    
    def show(self):
        '''prints list of items
        Inputs: None
        Returns: self.items
        '''
        print(self.items)
    
    def __str__(self):
        stackAsString = ''
        for item in self.items:
            stackAsString += str(item) + ' '
        return stackAsString
    
    def clear(self):
        '''clears list of items to empty
        Inputs: None
        Returns: None
        '''
        #TO DO: complete method according to updated ADT
        if len(self.items) != 0:
            while len(self.items) > 0:
                self.items.pop()
                
class Abostack:
    # Implement a class named AbacoStack to represent the AbacoStack structure
    # store bounded stacks and a list representing the top row. 
    # The size of the list will be the number of bounded stacks + 2. 
    # The number of bounded stacks and their common depth should be given as input to the constructor of this class. 
    # The structure should be initialized so that each stack has only one and unique colour (colours are represented by letters A, B, C, etc.). 
    # Another property of an instance of this class is to store the numbers of moves already done since the initialization    
    def __init__(self, nom_stacks, stack_depth):
        self.colours = ['A','B','C','D','E','F','G','H','I','J']
        self.nom_stacks = nom_stacks
        self.stack_depth = stack_depth
        self.top_row = []
        # stacks with colors
        self.stacks = []
        # creating stacks
        for stack in range(self.nom_stacks):
            self.stacks.append(BStack(self.stack_depth))
        # populate the stacks with colours
        for i in range(len(self.stacks)):
            for colour in range(self.stack_depth):
                self.stacks[i].push(self.colours[i])
        self.moves = 0
        # construct self.top_row
        for i in range(self.nom_stacks+2):
            self.top_row.append('.')
            
    def return_moves(self):
        '''returns number of moves that have been made
        Inputs: None
        Returns: moves (int)'''
        return self.moves    
            
    def check_invalid(self, move):
        '''checks if move made is valid for task 4
        Inputs: move (str)
        Returns: None
        '''
        valid = True
        if not (0 <= int(move[0]) <= self.nom_stacks and move[1] in ['u','d']) and not(0 <= int(move[0]) <= len(self.top_row) and move[1] in ['l','r']):
            valid = False
        stack_index = int(move[0]) -1
        if move[1] == 'u':
            if (self.stacks[stack_index].checkFull() and self.top_row[stack_index+1] != '.') or self.stacks[stack_index].checkEmpty():
                valid = False
        elif move[1] == 'd':
            if self.stacks[stack_index].checkFull():
                valid = False
        return valid
        
    def moveBead(self,move):
        '''changes the state of the AbacoStack instance based on the valid moves indicated above
        Inputs: move (str) - move made
        Retuens: None
        '''
        if not (0 <= int(move[0]) <= self.nom_stacks and move[1] in ['u','d']) and not(0 <= int(move[0]) <= len(self.top_row) and move[1] in ['l','r']):
            raise Exception('Error: Invalid Entry')
        # moving color along stackss
        if move[1] in ['u','d']:
            stack_index = int(move[0]) -1
            # moving the color up
            if move[1] == 'u':
                if (self.stacks[stack_index].checkFull() and self.top_row[stack_index+1] != '.') or self.stacks[stack_index].checkEmpty():
                    raise Exception('Invalid Move')
                if self.stacks[stack_index].peek() != '.' and self.top_row[stack_index+1] == '.':
                    color = self.stacks[stack_index].pop()
                    self.stacks[stack_index].push('.')
                    self.top_row[stack_index+1] = color
                else:
                    self.stacks[stack_index].moveColorUp()
                self.moves += 1
            # moving the color down
            elif move[1] == 'd':
                if self.stacks[stack_index].checkFull():
                    raise Exception('Invalid Move') 
                if self.top_row[stack_index+1] != '.' and self.stacks[stack_index].peek() == '.':
                    color = self.top_row[stack_index+1]
                    self.top_row[stack_index+1] = '.'
                    self.stacks[stack_index].pop()
                    self.stacks[stack_index].push(color)
                else:
                    self.stacks[stack_index].moveColorDown()
                self.moves += 1
            
        # moving color along the top row
        if move[1] in ['l','r']:
            row_index = int(move[0])
            # moving left along the top row
            if move[1] == 'l':
                if self.top_row[row_index-1] != '.' or self.top_row[row_index] == '.':
                    raise Exception('Invalid Move')                
                self.top_row[row_index -1] = self.top_row[row_index]
                self.top_row[row_index] = '.'
                self.moves += 1
            # moving  right along the top row
            elif move[1] == 'r' and (not self.top_row[row_index + 1] == 0 and self.top_row[row_index +1] == '.'):
                if self.top_row[row_index+1] != '.' or self.top_row[row_index] == '.':
                    raise Exception('Invalid Move')                  
                self.top_row[row_index +1] = self.top_row[row_index]
                self.top_row[row_index] = '.'   
                self.moves += 1 
    
    def isSolved(self,card):
        # returns TRUE if the state of the instance corresponds to the configuration card, FALSE otherwise
        card_stacks = []
        for card_stack in range(self.nom_stacks):
            card.stack(card_stack+1)[::-1]
            card_stacks.append(card.stack(card_stack+1)[::-1])
        
        player_card = []    
        for i in range(len(self.stacks)):
            crnt_stack = self.stacks[i].return_items_for_show()
            player_card.append(crnt_stack)
        return player_card == card_stacks
    
    def reset(self):
        '''resets the property moves to zero and rearrange the stack to the initial position with each stack having its own beads
        Inputs: None
        Returns: None'''
        self.moves = 0
        self.top_row = []
        for i in range(self.nom_stacks+2):
            self.top_row.append('.')        
        for i in range(len(self.stacks)):
            for colour in range(self.stack_depth):
                self.stacks[i].pop()
            for colour in range(self.stack_depth):
                self.stacks[i].push(self.colours[i])              
                
    def show(self,card= None): 
        '''that takes an optional parameter card and displays the state of the AbacoStack instance. 
        card is an instance of the class Card. When the parameter card is present, the configuration 
        card will also be displayed on the side of the AbacoStack instance in addition to the number of moves
        Inputs: card (Card) - goal card
        Returns: None'''
        # print card
        pos = 0
        for i in range(self.stack_depth+2): # printing the coordinates
            print(i, ' ', end='')
        print()
        for item in self.top_row: # print item in top_row list
            print(item,' ', end= '')
        print()
        for stack in range(self.stack_depth): # printing items in stack
            crnt_stack = 0                 
            print('|  ', end= '')
            for i in range(self.nom_stacks):
                bead = self.stacks[i].return_for_display()
                print(bead,' ', end = '')
                crnt_stack += 1
            print('|')
            pos += 1   
        print('+%s+' % ((len(self.top_row)+len(self.stacks)*2)*'-'))
        
        if card != None:
            stacks_split = card.return_stacks_split()
            # print card
            pos = 0
            for i in range(self.stack_depth+2): # printing the coordinates
                print(i, ' ', end='')
            print()
            for item in self.top_row: # print item in top_row list
                print(item,' ', end= '')
            print('    ', end = '')
            print('  card')
            print()
            for stack in range(self.stack_depth): # printing items in stack
                crnt_stack = 0                 
                print('|  ', end= '')
                for i in range(self.nom_stacks):
                    bead = self.stacks[i].return_for_display()
                    print(bead,' ', end = '')
                print('|', end = '')
                print('    ', end = '') # printing items in card
                print('| ', end= '')
                for bead in range(self.stack_depth):
                    print(stacks_split[crnt_stack][pos], end = ' ')
                    crnt_stack += 1
                print('|')                
                pos += 1   
            print('+%s+' % ((len(self.top_row)+len(self.stacks)*2)*'-'), end = '')
            print('            ', end= '')
            print(' %i moves'% (self.moves))
        
    
def main():
    # uncomment and run tests for testing
    
    ## testing for Card class
    card = Card(3,3)
    #card.replace('file.txt',1)
    #card.show()
    #print(card.stack(1))
    #print(card.stack(2))
    #print(card.stack(3))
    #card.reset()
    #card.show()
    
    ## BStack class testing
    #stack = BStack(3)
    #stack.push(3)
    #stack.push(2)
    #print(stack.isEmpty())
    #stack.pop()
    #print(stack)
    #print(stack.isFull())
    
    ## Abostack class testing
    #game = Abostack(3,3)
    #game.moveBead('1u')
    #game.moveBead('1l')
    #game.show()
    #game.moveBead('2u')
    #game.moveBead('2l')
    #game.moveBead('1d')
    #game.moveBead('0r')
    #game.show()
    #game.reset()
    #game.show() 
    #game.show(card)
    
    
    
if __name__ == "__main__":
    main()