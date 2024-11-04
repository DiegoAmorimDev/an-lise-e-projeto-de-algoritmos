import time
time1 = time.time()

def Maxi(A):
    x = A[0] 
    print(f"Valor inicial: {x}")  # Mostra o valor inicial
    
    for i in range(len(A)):
        if A[i] > x:
            x = A[i]
            print(f"Valor máximo atual: {x} (índice {i})")  # Exibe o novo máximo
            
    return x

A = list(range(1, 101))

resultado_final = Maxi(A)

time2 = time.time()
time3 = (time2 - time1)*1000


print(f"\nResultado final: {resultado_final}")
print(f"\nTempo de execução: {time3} milisegundos")
