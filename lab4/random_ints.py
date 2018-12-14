import sys
import random

with open(sys.argv[1], 'w') as f:
    for _ in range(int(sys.argv[2])):
        f.write(str(random.randint(-5000,5000)) + '\n')
