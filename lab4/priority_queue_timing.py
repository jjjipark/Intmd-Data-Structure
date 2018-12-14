from heapq import *
import sys
import timeit

# this implements a priority queue on top of the builtin python list type
# offers O(1) inserts and O(n) removes
class BadPriorityQueue:

    def __init__(self):
        self.q = []

    def is_empty(self):
        return not bool(self.q)

    def insert(self, x):
        self.q.append(x)  # O(1) [amortized]

    def remove_min(self):
        min_elmt = min(self.q)  # O(n)
        self.q.remove(min_elmt)  # O(n)
        return min_elmt  # total runtime is O(n)

# this implements a priority queue on top of a binary (min) heap
# offers O(log n) inserts and O(log n) removes
class PriorityQueue:

    def __init__(self):
        self.q = []

    def is_empty(self):
        return not bool(self.q)

    def insert(self, x):
        heappush(self.q, x)  # O(log n)

    def remove_min(self):
        return heappop(self.q)  # O(log n)

# queue is an empty priority queue object that exposes the methods insert(x), is_empty(),
# and remove_min()
def priority_queue_sort(unsorted_list, queue):
    # insert each integer into the priority queue
    for x in unsorted_list:
        queue.insert(x)

    # remove min until the priority queue is empty
    sorted_list = []
    while not queue.is_empty():
        sorted_list.append(queue.remove_min())

    return sorted_list

def read_ints_into_list(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    return list(map(lambda t: int(t.strip()), lines))

def write_ints_list(int_list, filename):
    with open(filename, 'w') as f:
        for x in int_list:
            f.write(str(x) + "\n")

if __name__ == "__main__":
    int_list = read_ints_into_list(sys.argv[1])

    # sort with the bad priority queue
    start = timeit.default_timer()
    sorted1 = priority_queue_sort(int_list, BadPriorityQueue())
    end = timeit.default_timer()
    write_ints_list(sorted1, "bad_sort")
    print("Time with O(n^2) sort:", end - start)

    # sort with the good priority queue
    start = timeit.default_timer()
    sorted2 = priority_queue_sort(int_list, PriorityQueue())
    end = timeit.default_timer()
    write_ints_list(sorted2, "good_sort")
    print("Time with O(n * log n) sort:", end - start)
