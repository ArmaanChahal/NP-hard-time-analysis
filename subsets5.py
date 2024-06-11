#this iterates it once, the other python file does it over multiple iterations
from itertools import combinations
import time

start=time.time()
numbers = [-12, -3, -6, 7, 2, -2, 6, 3, 9, -7, -5, -8, 1, 11, -9, -4]
total = 0

for s in range(1, 6):
    subset_size = s
    subsets = list(combinations(numbers, subset_size))
    subsets_0 = [subset for subset in subsets if sum(subset) == 0]
    total += len(subsets_0)

end=time.time()
print("Total subsets of 0: ", total)
print("time taken: ", end-start)
