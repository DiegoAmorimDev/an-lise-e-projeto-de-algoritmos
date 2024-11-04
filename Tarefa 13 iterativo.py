import time

def fib_iterative(n):
    if n <= 1:
        return n
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[n]

n_values = [10, 20, 30, 50, 100]

for n in n_values:
    start_time = time.time()
    result = fib_iterative(n)
    end_time = time.time()
    print(f"Fib({n}) = {result} (Iterativo) - Tempo: {end_time - start_time:.6f} segundos")
