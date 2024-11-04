import time
import random

time1 = time.time()

def decide_I(A, n, x):
    i = 1 
    while i <= n and A[i - 1] != x: 
        print(f"Verificando o elemento A[{i - 1}]: {A[i - 1]}")
        i += 1

    if i > n:
        return "NÃO"
    else:
        return "SIM"

A = [random.randint(1, 100) for _ in range(100)]  
n = 100
x = random.choice(A)  

print(f"Lista A: {A}")
print(f"Valor que vamos procurar: {x}")

resultado = decide_I(A, n, x)
print(resultado) 

time2 = time.time()
time3 = (time2 - time1) * 1000

print(f"O tempo de execução foi: {time3} milissegundos")
