from heapq import heappush, heappop
import sys
import itertools

def heapSort(heap):

    return [heappop(heap)[2][0] for i in range(len(heap))]


def printIP(heap):
    for i in heap:
        print i


def driver():

    with open(sys.argv[1]) as f:
    #with open(raw_input("Enter Filename: "), 'r') as f:
        n = int(f.readline().strip())
        heapA = []
        heapB = []
        counter = itertools.count()
        for _ in range(n):
            in_data = f.readline().strip().split()
            IP, Tier, Time = in_data[0], in_data[1], int(in_data[2])
            if Tier == "A":
                count = next(counter)
                heappush(heapA, (Time, count, in_data))
                #pop_task()
            if Tier == "B":
                #B.append((Time, in_data))
                count = next(counter)
                heappush(heapB, (Time, count, in_data))

        printIP(heapSort(heapA))
        printIP(heapSort(heapB))


if __name__ == "__main__":
    driver()



'''
10.31.99.245 B 30
10.16.0.105 A 150
10.16.115.160 B 60
10.30.111.90 B 65
10.16.0.105 A 20
10.30.100.100 A 25
10.16.100.115 A 150
10.111.111.119 B 60

10.16.0.105
10.30.100.100
10.16.0.105
10.16.100.115

10.31.99.245
10.16.115.160
10.111.111.119
10.30.111.90
'''