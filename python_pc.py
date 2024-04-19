import math
import random
from multiprocessing import Pool
import time

def compute_pi(n, num_processes):
    chunk_size = n // num_processes
    pool = Pool(processes=num_processes)
    results = []
    for _ in range(num_processes):
        result = pool.apply_async(monte_carlo_pi, args=(chunk_size,))
        results.append(result)
    pool.close()
    pool.join()

    total_in_circle = sum(result.get() for restult in results)
    return 4 * total_in_circle / n

def monte_carlo_pi(chunk_size):
    count_in_circle = 0
    for _ in range(chunk_size):
        x = random.random()
        y = random.random()
        if x**2 + y**2 <= 1:  # Check if point falls inside the circle
            count_in_circle += 1
    return count_in_circle

n = 1_000_000
num_processes = 4
approx_pi = compute_pi(n, num_processes)
print(f"Approximation of pi: {approx_pi}")
