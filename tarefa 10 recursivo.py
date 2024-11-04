import time

A = list(range(101))
n = len(A)
x = 20  

time1 = time.time()

def decideR(A, n, x):
    if n < 0:
        print(f"NÃO")
        return
    print(f"Verificando índice {n}: valor {A[n]}")  
    if A[n] == x:
        print(f"SIM")
        return

    decideR(A, n - 1, x)

decideR(A, n - 1, x)

time2 = time.time()
time3 = (time2 - time1) * 1000

print(f"O tempo de execução foi: {time3:.2f} milissegundos")
