from collections import deque

arcos = [
    (0, 1), (1, 2), (1, 3), (3, 4), (3, 5), (1, 6),
    (0, 7), (7, 8), (7, 9), (8, 6)
]

grafo = {}
for u, v in arcos:
    if u not in grafo:
        grafo[u] = []
    if v not in grafo:
        grafo[v] = []
    grafo[u].append(v)
    grafo[v].append(u)  # Se o grafo for não direcionado

grafo_lista = {
    0: [1, 4],
    1: [2, 5],
    2: [3],
    3: [7],
    4: [8],
    5: [4],
    6: [5, 10, 2],
    7: [11, 6],
    8: [9],
    9: [5, 8],
    10: [9],
    11: [10]
}

def GRAPHbfs(grafo, inicio):
    visitados = set()  
    fila = deque([inicio])  
    rastreamento = []  

    while fila:
        vertice = fila.popleft()
        if vertice not in visitados:
            visitados.add(vertice)  
            rastreamento.append(vertice)  
            fila.extend(neighbor for neighbor in grafo[vertice] if neighbor not in visitados)

    return rastreamento

def GRAPHdfs(grafo, inicio, visitados=None, rastreamento=None):
    if visitados is None:
        visitados = set()
    if rastreamento is None:
        rastreamento = []

    visitados.add(inicio)  
    rastreamento.append(inicio) 

    for neighbor in grafo[inicio]:
        if neighbor not in visitados:
            GRAPHdfs(grafo, neighbor, visitados, rastreamento)

    return rastreamento

# Executar a busca em largura
print("Busca em Largura (BFS):")
bfs_rastreamento = GRAPHbfs(grafo, 0)
print("Rastreamento:", bfs_rastreamento)

# Executar a busca em profundidade
print("\nBusca em Profundidade (DFS):")
dfs_rastreamento = GRAPHdfs(grafo, 0)
print("Rastreamento:", dfs_rastreamento)

# Executar BFS e DFS na lista de adjacências
print("\nBusca em Largura (BFS) na lista de adjacência:")
bfs_lista_rastreamento = GRAPHbfs(grafo_lista, 0)
print("Rastreamento:", bfs_lista_rastreamento)

print("\nBusca em Profundidade (DFS) na lista de adjacência:")
dfs_lista_rastreamento = GRAPHdfs(grafo_lista, 0)
print("Rastreamento:", dfs_lista_rastreamento)
