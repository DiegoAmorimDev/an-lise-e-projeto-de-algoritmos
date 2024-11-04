
grafo = {
    0: [0, 2],
    1: [3, 3],
    2: [6],
    3: [7],
    4: [],
    5: [],
    6: [0, 4, 2],
    7: [5],
    8: []
}


print("Lista de adjacências:")
for vertice, adjacencias in grafo.items():
    print(f"{vertice}: {', '.join(map(str, adjacencias))}")
