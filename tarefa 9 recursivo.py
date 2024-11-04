import time

time1=time.time()
def Maxi(A, n):
    if n == 1:
        print(f"Valor inicial: {A[0]}")
        return A[0]
    
    x = Maxi(A, n - 1)

    print(f"Valor máximo atual: {x} (índice {n - 1})") 

    if x < A[n - 1]:
        return A[n - 1]
    else:
        return x

A = list(range(1, 101))
n = len(A)

resultado_final = Maxi(A, n)
time2=time.time()
time3= (time2 - time1)*1000

print(f"\nResultado final: {resultado_final}")

print(f"\nTempo de execução: {time3} milisegundos")
