def somaesq(n, A):
    if A == 0:
        return 0
    
    resultp = somaesq(n, A - 1) + n[A]
    
    print(f"Soma parcial (índice {A}): {resultp}")
    return resultp

n = list(range(1, 101))

resultado_final = somaesq(n, len(n) - 1)

print(f"\nResultado final: {resultado_final}")
        
