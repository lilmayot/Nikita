#На вход первой строкой числа n ( 1<=n<=100) –
# количество вершин в графе и m ( 1$ le$m$ le$n(n - 1)/2) – количество ребер.
#следующими строками m пар чисел – ребра графа. Пример ниже
#5 2
#1 3
#2 3

list_reber = []

def AdjacencyMatrix(a,b):
    global list_reber
    adj = [[0] * a for _ in range(a)]

    for it in range(b):
        r, c = map(int, input().split())
        list_reber.append([r, c])
        adj[r - 1][c - 1] = adj[c - 1][r - 1] = 1
    print("Матрица Смежности")
    return adj

def AdjacencyList(a, b):
    # Список смежности
    for i in range(a):
        print("V" + str(i) + ":", end=" ")
        for j in range(a):
            if b[i][j] == 1:
                print("V" + str(j), end=" ")
        print()

def IncidenceMatrix(a,b):
    global list_reber
    count_reber = b
    count_vershin = a

    matrix = [[0] * count_vershin for i in range(count_reber)]

    for i in range(count_reber):
        for j in range(count_vershin):
            if list_reber[i][0] == j + 1 or list_reber[i][1] == j + 1:
                matrix[i][j] = 1
            else:
                matrix[i][j] = 0

    return matrix


print("Введите количество вершин в графе и количество ребер через пробел(пример):0 0\n")
n, m = map(int, input().split())
print("Введите парами ребра графа через пробел\n")
d = AdjacencyMatrix(n, m)
print(d)
print("Список Смежности")
AdjacencyList(n, d)
print("Матрица Инцидентности")
print(IncidenceMatrix(n, m))
