import tracemalloc
import os
import psutil

tracemalloc.start()
process = psutil.Process(os.getpid())

def inspect_mem(label=""):
    current, peak = tracemalloc.get_traced_memory()
    rss = process.memory_info().rss / (1024 ** 2)
    print(f"\n--- Memory: {label} ---")
    print(f"Python current allocations: {current / 1024**2:.2f} MB")
    print(f"Python peak allocations:    {peak / 1024**2:.2f} MB")
    print(f"Process RAM (RSS):          {rss:.2f} MB")
    print('-----')
