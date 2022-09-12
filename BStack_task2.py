# task 2 - Implement a Bounded Stack with isFull() method
# Author: Saumya Rada

class BStack:
    def __init__(self, capacity):
        assert isinstance(capacity, int), ('Error: Type error: %s' % (type(capacity)))
        assert capacity > 0, ('Error: Illegal capacity: %d' % (capacity)) 
        
        self.items = []
        self.capacity = capacity
        self.accesses = 0
    def push(self, item):
        if len(self.items) >= self.capacity:
            raise Exception('Error: Queue is full')
        self.items.append(item)
    
    # MODIFY: RAISE AN EXCEPTION IF THIS METHOD IS INVOKED ON AN EMPTY STACK
    def pop(self): 
        if len(self.items) <= 0:
            raise Exception('Error: Queue is empty')
        return self.items.pop() 
    
    # MODIFY: RAISE AN EXCEPTION IF THIS METHOD IS INVOKED ON AN EMPTY STACK
    def peek(self):
        if len(self.items) <= 0:
            raise Exception('Error: Queue is empty')        
        return self.items[len(self.items)-1]
    
    def return_for_display(self):
        if self.accesses == self.capacity:
            self.accesses = 1
        else:
            self.accesses += 1
        return self.items[len(self.items)-self.accesses]
    
    def return_items_for_show(self):
        return self.items
    
    def isEmpty(self):
        return self.items == []
    
    def isFull(self):
        return len(self.items) == self.capacity
    
    def size(self):
        return len(self.items)
    
    def show(self):
        print(self.items)
    
    def __str__(self):
        stackAsString = ''
        for item in self.items:
            stackAsString += item + ' '
        return stackAsString
    
    def clear(self):
        #TO DO: complete method according to updated ADT
        if len(self.items) != 0:
            while len(self.items) > 0:
                self.items.pop()