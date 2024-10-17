
class Queue:
    """Queue implementation as a list"""

    def __init__(self):
        """Create new queue"""
        self._items = {}                  

    def is_empty(self):
        """Check if the queue is empty"""
        return not bool(self._items)

    def enqueue(self, item):
        """Add an item to the queue"""
        x = len(self._items)
        self._items[x] = item
        return self._items  

    def dequeue(self):
        """Remove an item from the queue"""
        if len(self._items) > 0:
            return self._items.pop(0)
        else:
            raise RuntimeError("Trying to dequeue from an empty queue")

    def size(self):
        """Get the number of items in the queue"""
        return len(self._items)

    def __str__(self):
        return str(self._items)
    
def main():
    q = Queue()
    try:
        q.enqueue('a')
        print(q.enqueue(65))
        print(q.enqueue('hamburgar'))
        print(q.dequeue())
        print(q.size())
        print(q)
        
        
        
       
        
    except RuntimeError as e:
        print("I have an error!")
        print(e)
main()
