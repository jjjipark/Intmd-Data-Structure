import sys
import copy
from linked_list import *

class Stack:

    # class constructor
    def __init__(self):
        self.l = LinkedList()

    # push method
    def push(self, x):
        self.l.add_at_head(x)

    # pop method
    def pop(self):
        return self.l.remove_at_head()

    # is_empty method
    def is_empty(self):
        return self.l.is_empty()

def print_stack(s):
    if s.is_empty():
        print "Empty"
        return
    c = copy.deepcopy(s)
    res = []
    while not c.is_empty():
        res.append(c.pop())
    print ' '.join(map(str, res))
    return

# this function runs the program according to the problem specification
def driver():
    s = Stack()
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        for _ in range(n):
            in_data = f.readline().strip().split()
            action, value_option = in_data[0], in_data[1:]
            if action == "push":
                value = int(value_option[0])
                s.push(value)
            elif action == "pop":
                try:
                    print(s.pop())
                except EmptyListError:
                    print 'StackError'
            elif action == "print":
                print_stack(s)

if __name__ == "__main__":
    driver()
