import heapq  # Importa o módulo heapq para usar a fila de prioridade

# Representação do grafo como um dicionário de dicionários, onde as chaves são vértices e os valores são os pesos das arestas
grafo = {
    'a': {'b': 16, 'f': 21, 'e': 9},
    'b': {'c': 5, 'd': 6, 'f': 11},
    'c': {},
    'd': {'c': 10},
    'e': {'d': 18, 'f': 33},
    'f': {'b': 11, 'd': 14}
}

# Implementação do Algoritmo de Dijkstra
def algoritmo_dijkstra(grafo, vertice_inicial, vertice_final):
    # Dicionário para armazenar as distâncias mínimas de cada vértice, inicializado como infinito
    distancias = {vertice: float('inf') for vertice in grafo}
    distancias[vertice_inicial] = 0  # A distância da origem para si mesma é zero
    # Dicionário para armazenar o caminho anterior de cada vértice
    caminho_anterior = {vertice: None for vertice in grafo}

    # Criação de uma fila de prioridade para explorar os vértices
    fila_prioridade = [(0, vertice_inicial)]  # Tupla com distância e vértice inicial

    while fila_prioridade:
        # Remove o vértice com a menor distância da fila
        distancia_atual, vertice_atual = heapq.heappop(fila_prioridade)

        # Se o vértice atual é o destino, finaliza a busca
        if vertice_atual == vertice_final:
            break

        # Examina todos os vizinhos do vértice atual
        for vizinho, peso in grafo[vertice_atual].items():
            # Calcula a nova distância para o vizinho
            nova_distancia = distancia_atual + peso

            # Se uma distância menor é encontrada, atualiza as estruturas
            if nova_distancia < distancias[vizinho]:
                distancias[vizinho] = nova_distancia
                caminho_anterior[vizinho] = vertice_atual
                heapq.heappush(fila_prioridade, (nova_distancia, vizinho))

    # Reconstrução do caminho mínimo a partir do vértice final
    caminho_minimo = []
    atual = vertice_final
    while atual is not None:
        caminho_minimo.insert(0, atual)  # Adiciona o vértice ao início do caminho
        atual = caminho_anterior[atual]  # Move-se para o vértice anterior

    # Custo total do caminho até o destino
    custo_total = distancias[vertice_final]
    return caminho_minimo, custo_total

# Definição dos vértices de partida e chegada
vertice_inicial = 'a'
vertice_final = 'c'

# Execução do Algoritmo de Dijkstra para encontrar o caminho de 'a' até 'c'
caminho_encontrado, custo_total_encontrado = algoritmo_dijkstra(grafo, vertice_inicial, vertice_final)

# Apresentação do resultado
print("\nCaminho encontrado pelo Algoritmo de Dijkstra:")
print(" -> ".join(caminho_encontrado))
print(f"Custo total: {custo_total_encontrado}")
