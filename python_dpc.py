from mpi4py import MPI
import math
import time

def f(x):
    return math.sqrt(1 - x**2)

def compute_partial_sum(start, end, n):
    dx = 1.0 / n
    partial_sum = 0
    for i in range(start, end):
        x = i * dx
        partial_sum += f(x) * dx
    return partial_sum

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

n = 1_000_000  

chunk_size = n // size
remainder = n % size
if remainder != 0:
    if rank < remainder:
        chunk_size += 1

start = rank * chunk_size
end = start + chunk_size

partial_sum = compute_partial_sum(start, end, n)
total_sum = comm.reduce(partial_sum, op=MPI.SUM, root=0)

if rank == 0:
    approx_pi = 4 * total_sum
    print(f"Approximation of pi: {approx_pi}")

comm.barrier()
