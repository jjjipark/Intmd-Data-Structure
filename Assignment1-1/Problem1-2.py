import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:

    # class constructor
    def __init__(self):
        self.first = None
        self.last = None

    # push method
    def enqueue(self, data):
        new_data = Node(data)
        if self.first is None and self.last is None:
            self.first = new_data
            self.last = self.first

        else:
            self.last.next = new_data
            self.last = new_data

    # pop method
    def dequeue(self):
            if self.is_empty():
                print("QueueError")
                exit()
            else:
                popped = str(self.first.data)
                if self.first.next is None:
                    self.first = None
                    #self.last = None
                else:
                    self.first = self.first.next
                return popped


    # is_empty method
    def is_empty(self):
        return True if self.first is None else False

    def print_queue(self):
        if self.is_empty():
            print("Empty")
        else:
            value = self.first
            while value is not None:
                print value.data,
                value = value.next
            print('')

#a = Queue()
#a.enqueue(1)
#a.enqueue(2)
#q.enqueue(3)
#a.printqueue()
#a.dequeue()
#print("\n")
#q.printqueue()

def driver():
    q = Queue()
    ##with open(sys.argv[1]) as f:
    with open(raw_input("Enter Filename: "), 'r') as f:
        n = int(f.readline().strip())
        for _ in range(n):
            in_data = f.readline().strip().split()
            #print(in_data)
            action, value_option = in_data[0], in_data[1:]
            if action == "enqueue":
                value = int(value_option[0])
                q.enqueue(value)
            elif action == "print":
                 q.print_queue()

            elif action == "dequeue":
                return_value = q.dequeue()
                print(return_value)

if __name__ == "__main__":
    driver()