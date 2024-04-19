import math
import time

def f(x):
    return math.sqrt(1 - x**2)

def compute_pi(n):
    dx = 1.0 / n
    sum = 0
    for i in range(n):
        x = i * dx
        sum += f(x) * dx
    return 4 * sum

n = 1_000_000
approx_pi = compute_pi(n)
print(f"Approximation of pi: {approx_pi}")