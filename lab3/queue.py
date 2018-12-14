import sys
import copy
from linked_list import *

class Queue:

    def __init__(self):
        self.l = LinkedList()

    def enqueue(self, x):
        self.l.add_at_tail(x)

    def dequeue(self):
        return self.l.remove_at_head()


    def is_empty(self):
        return self.l.is_empty()

def print_queue(q):
    if q.is_empty():
        print "Empty"
        return
    c = copy.deepcopy(q)
    res = []
    while not c.is_empty():
        res.append(c.dequeue())
    print ' '.join(map(str, res))
    return

def driver():
    q = Queue()
   # with open(sys.argv[1]) as f:
    with open(raw_input("Enter Filename: "), 'r') as f:
        n = int(f.readline().strip())
        for _ in range(n):
            in_data = f.readline().strip().split()
            action, value_option = in_data[0], in_data[1:]
            if action == "enqueue":
                value = int(value_option[0])
                q.enqueue(value)
            elif action == "dequeue":
                try:
                    print(q.dequeue())
                    print type(q.dequeue())
                except EmptyListError:
                    print 'QueueError'
            elif action == "print":
                print_queue(q)

if __name__ == "__main__":
    driver()
