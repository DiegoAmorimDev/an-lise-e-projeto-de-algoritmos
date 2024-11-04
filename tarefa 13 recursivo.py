import time

def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

# Teste para valores de n
n_values = [10, 20, 30, 50, 100]
for n in n_values:
    start_time = time.time()
    result = fib_recursive(n)
    end_time = time.time()
    print(f"Fib({n}) = {result} (Recursivo) - Tempo: {end_time - start_time:.6f} segundos")
