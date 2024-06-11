from itertools import combinations
import random
import time
import csv

# Function to generate random numbers
def generate_random_numbers(n, lower=-50, upper=50):
    return [random.randint(lower, upper) for _ in range(n)]

# Initial set of numbers
numbers = [-12, -3, -6, 7, 2, -2, 6, 3, 9, -7, -5, -8, 1, 11, -9, -4]

# Open CSV file to store the results
with open('time_taken.csv', 'w', newline='') as csvfile:
    fieldnames = ['iteration', 'num_elements', 'time_taken']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for iteration in range(20):  # 100 iterations
        start = time.time()
        
        total = 0
        for s in range(1, 6):
            subset_size = s
            subsets = list(combinations(numbers, subset_size))
            subsets_0 = [subset for subset in subsets if sum(subset) == 0]
            total += len(subsets_0)
        
        end = time.time()
        time_taken = end - start
        
        # Write results to CSV
        writer.writerow({'iteration': iteration + 1, 'num_elements': len(numbers), 'time_taken': time_taken})
        
        # Add 100 random numbers to the set
        numbers.extend(generate_random_numbers(5))

print("Process completed. Time taken for each iteration has been stored in 'time_taken.csv'.")
