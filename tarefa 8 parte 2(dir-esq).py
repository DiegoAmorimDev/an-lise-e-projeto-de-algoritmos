def somadir(n, A):
    if A == len(n):
        return 0
    
    resultp = somadir(n, A + 1) + n[A]
    
    print(f"Soma parcial (índice {A}): {resultp}")
    return resultp

n = list(range(1, 101))

resultado_final = somadir(n, 0)

print(f"\nResultado final: {resultado_final}")