

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    # class constructor
    def __init__(self):
        self.head = None

     # push method
    def push(self, data):
        top = Node(data)        #adding front
        top.next = self.head
        self.head = top
        #print(data)

    # pop method
    def pop(self):
        ##removing from same side as adding
        if self.is_empty():
            print("StackError")
            exit()
        else:
            popped = self.head.data
            self.head = self.head.next
            return str(popped)

  # is_empty method
    def is_empty(self):
        return True if self.head is None else False

    def print_stack(self):
        #top = self.head
        if self.is_empty():
            print("Empty")
        else:
            value = self.head
            while value is not None:
                print value.data,
                value = value.next
            print('')

# this function runs the program according to the problem specification
def driver():
    s = Stack()
    ##with open(sys.argv[1]) as f:
    with open(raw_input("Enter Filename: "), 'r') as f:
        n = int(f.readline().strip())
        print n
        for _ in range(n):
            in_data = f.readline().strip().split()
            action, value_option = in_data[0], in_data[1:]
            if action == "push":
                value = (value_option[0])
                s.push(value)
                #print(0)  # change this!
            elif action == "pop":
                return_value = s.pop()
                print type(return_value)
                print return_value # change this!
            elif action == "print":
                s.print_stack()
                #print("need to implement print")  # change this!


# this starter code should work with either python or python3
if __name__ == "__main__":
    driver()
