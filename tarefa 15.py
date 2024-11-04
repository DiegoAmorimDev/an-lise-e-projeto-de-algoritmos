import sys

# Define Maxn como 10
Maxn = 10
INT_MAX = sys.maxsize

def main():
    b = [0] * (Maxn + 1)
    m = [[0] * Maxn for _ in range(Maxn)]

    n = int(input("Número de matrizes n: "))

    print("Dimensões das matrizes: ")
    for i in range(n + 1):
        b[i] = int(input())

    for i in range(n):
        m[i][i] = 0

    for h in range(1, n):
        for i in range(1, n - h + 1):
            j = i + h
            m[i-1][j-1] = INT_MAX
            for k in range(i, j):
                temp = m[i-1][k-1] + m[k][j-1] + b[i-1] * b[k] * b[j]
                if temp < m[i-1][j-1]:
                    m[i-1][j-1] = temp

            print(f"m[{i-1}][{j-1}] = {m[i-1][j-1]}")

    print('\n')

if __name__ == "__main__":
    main()