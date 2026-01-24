import pytest

@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (0, 5, 5),
    (-1, 1, 0)
])
def test_add(a, b, expected):
    assert a + b == expected


# --------------------------------------------------------------------


from collections import deque, defaultdict

# -------------------------
# Класс Graph (для примера)
# -------------------------
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = defaultdict(list)

    def add_edge(self, u, v):
        self.adj[u].append(v)

    def bfs(self, start):
        visited = [False] * self.V
        queue = deque([start])
        visited[start] = True
        result = []
        while queue:
            node = queue.popleft()
            result.append(node)
            for neighbor in self.adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        return result

# -------------------------
# Fixture — создаёт граф
# -------------------------
@pytest.fixture
def sample_graph():
    g = Graph(6)
    g.add_edge(5, 2)
    g.add_edge(5, 0)
    g.add_edge(4, 0)
    g.add_edge(4, 1)
    g.add_edge(2, 3)
    g.add_edge(3, 1)
    return g

# -------------------------
# Parametrize — разные входные вершины
# -------------------------
@pytest.mark.parametrize("start, expected_bfs", [
    (5, [5, 2, 0, 3, 1]),
    (4, [4, 0, 1]),
    (2, [2, 3, 1]),
])
def test_bfs(sample_graph, start, expected_bfs):
    assert sample_graph.bfs(start) == expected_bfs
