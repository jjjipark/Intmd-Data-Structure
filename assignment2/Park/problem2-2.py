import heapq
import sys
class Median:

    def __init__(self):
        self.first_half = []      #min_heap
        self.second_half = []     #max_heap

    def insert(self, item):
        if self.first_half == [] or item < -self.first_half[0]:
            heapq.heappush(self.first_half, -item)    
        else:
            heapq.heappush(self.second_half, item)
        self.rebalance()


    def rebalance(self):
        first_len = len(self.first_half)
        second_len = len(self.second_half)
        if first_len - second_len > 1:                  #
            elt = -heapq.heappop(self.first_half)     
            heapq.heappush(self.second_half, elt)
        elif second_len - first_len > 1:
            elt = -heapq.heappop(self.second_half)
            heapq.heappush(self.first_half, elt)

    def median(self):
        first_len = len(self.first_half)
        second_len = len(self.second_half)
        if first_len > second_len:
            result = -self.first_half[0]
        elif second_len > first_len:
            result = self.second_half[0]
        else:
            result = -self.first_half[0] + self.second_half[0]
            if result %2 ==0:
                result = result/2
            else:
                result = round((result/2.0), 1)
        return result


def driver():
    s = Median()
    with open(sys.argv[1]) as f:
    #with open(raw_input("Enter Filename: "), 'r') as f:
        n = int(f.readline().strip())
        for _ in range(n):
            in_data = f.readline().strip().split()
            value = int(in_data[0])
            s.insert(value)
            print s.median()


if __name__ == "__main__":
    driver()
