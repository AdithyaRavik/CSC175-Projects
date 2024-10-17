#1a. It results in an IndexError because we are poping from an empyt list
#1b. Results in an IndexError because list index is out of range


class Stack2:
    """Stack implementation as a list"""

    def __init__(self):
        """Create new stack"""
        self._items = []

    def is_empty(self):
        """Check if the stack is empty"""
        return not bool(self._items)

    def push(self, item):
        """Add an item to the stack"""
        self._items.append(item)

    def pop(self):
        """Remove an item from the stack"""
        if len(self._items) == 0:
            raise Exception("Error! Popping from an exmpty stack")
        else:
            return self._items.pop()
        

    def peek(self):
        """Get the value of the top item in the stack"""

        if len(self._items) == 0:
            raise Exception("Error! Peeking from an exmpty stack")
        else:
            return self._items[-1]

    def size(self):
        """Get the number of items in the stack"""
        return len(self._items)



def main():
    a = Stack2()
    try:
        print(a.pop())
    except Exception as e:
        print("Error!")
        print(e)
    try:
        print(a.peek())
    except Exception as f:
        print(f)

main()

#3a. Can't detect programmatically and user only sees error on screen
#3b. User may want to save None as an actual value in the data structure
#3c. Shows confusing message, could leak sensitive information and lead to security vulnerability
        
