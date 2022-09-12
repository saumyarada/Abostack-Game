# Assignment 3 - Task 1 (The Card Class)
# class named Card representing a configuration card. 
# An instance of this class should have one private property, beads a list storing in order the beads in each stack
# reset() to reshuffle the card to generate a new configuration, show() to display a card, and stack(number) to return the ordered list of elements top to bottom in the number stack

import random

class Card():
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
        
    def reset(self):
        random.shuffle(self.beads)
        
    def show(self):
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
        for stack in range(self.nom_stacks):
            crnt_stack = 0
            print('|', end= '')
            for bead in range(self.depth_stacks):
                print(stacks_split[crnt_stack][pos], end = '')
                crnt_stack += 1
            print('|')
            pos += 1

            
    def stack(self,number):
        start_index = (number - 1) * self.depth_stacks 
        end_index = start_index + self.depth_stacks 
        stack = []
        for bead in range(start_index, end_index):
            stack.append(self.beads[bead])
        return stack
    
def main():
    
    card = Card(3,3)
    card.show()
    print(card.stack(3))
    
    
    
    
if __name__ == "__main__":
    main()