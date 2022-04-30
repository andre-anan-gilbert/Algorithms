"""An implementation of an iterative breadth first search."""
from collections import deque


class BreadthFirstSearchIterative:
    """Class that implements an iterative breadth first search."""

    class _Edge:
        """Class that represents an edge in the graph.

        Attributes:
            fr: From edge.
            to: To edge.
            cost: Cost of the edge.
        """

        def __init__(self, fr: int, to: int, cost: int) -> None:
            self.fr = fr
            self.to = to
            self.cost = cost

    def __init__(self, graph: list[list[_Edge]]) -> None:
        if graph is None: raise ValueError('Graph cannot be None')
        self._n = len(graph)
        self._graph = graph
        self._prev = []

    def reconstruct_path(self, start: int, end: int) -> list[int]:
        """Reconstructs the path from node 'start' to 'end'.

        Returns:
            An array containing node indexes of the shortest path from 'start' to 'end'.
            If 'start' and 'end' are not connected then the path is empty.
        """
        self.bfs(start)
        path = []

        at = end
        while at is not None:
            path.append(at)
            at = self._prev[at]

        path.reverse()
        if path[0] == start: return path
        path.clear()
        return path

    def bfs(self, start: int) -> None:
        """Performs an iterative breadth first search starting at some node."""
        self._prev = [None for _ in range(self._n)]
        visited = [False for _ in range(self._n)]
        queue = deque()

        queue.append(start)
        visited[start] = True

        while queue:
            node = queue.popleft()
            edges = self._graph[node]

            for edge in edges:
                if not visited[edge.to]:
                    visited[edge.to] = True
                    self._prev[edge.to] = node
                    queue.append(edge.to)

    @staticmethod
    def create_empty_graph(n: int) -> list[list[_Edge]]:
        """Creates an empty adjacency list with n nodes."""
        return [[] for _ in range(n)]

    @staticmethod
    def add_directed_edge(graph: list[list[_Edge]], u: int, v: int, cost: int) -> None:
        """Adds a directed edge from node 'u' to 'v' with cost 'cost'."""
        graph[u].append(BreadthFirstSearchIterative._Edge(u, v, cost))

    @staticmethod
    def add_undirected_edge(graph: list[list[_Edge]], u: int, v: int, cost: int) -> None:
        """Adds an undirected edge between node 'u' and 'v' with cost 'cost'."""
        BreadthFirstSearchIterative.add_directed_edge(graph, u, v, cost)
        BreadthFirstSearchIterative.add_directed_edge(graph, u=v, v=u, cost=cost)

    @staticmethod
    def add_unweighted_undirected_edge(graph: list[list[_Edge]], u: int, v: int) -> None:
        """Adds an undirected edge between node 'u' and node 'v'."""
        BreadthFirstSearchIterative.add_undirected_edge(graph, u, v, 1)

    @staticmethod
    def format_path(path: list[int]) -> str:
        return ' -> '.join(map(str, path))


def main() -> None:
    n = 13
    graph = BreadthFirstSearchIterative.create_empty_graph(n)

    BreadthFirstSearchIterative.add_unweighted_undirected_edge(graph, 0, 7)
    BreadthFirstSearchIterative.add_unweighted_undirected_edge(graph, 0, 9)
    BreadthFirstSearchIterative.add_unweighted_undirected_edge(graph, 0, 11)
    BreadthFirstSearchIterative.add_unweighted_undirected_edge(graph, 7, 11)
    BreadthFirstSearchIterative.add_unweighted_undirected_edge(graph, 7, 6)
    BreadthFirstSearchIterative.add_unweighted_undirected_edge(graph, 7, 3)
    BreadthFirstSearchIterative.add_unweighted_undirected_edge(graph, 6, 5)
    BreadthFirstSearchIterative.add_unweighted_undirected_edge(graph, 3, 4)
    BreadthFirstSearchIterative.add_unweighted_undirected_edge(graph, 2, 3)
    BreadthFirstSearchIterative.add_unweighted_undirected_edge(graph, 2, 12)
    BreadthFirstSearchIterative.add_unweighted_undirected_edge(graph, 12, 8)
    BreadthFirstSearchIterative.add_unweighted_undirected_edge(graph, 8, 1)
    BreadthFirstSearchIterative.add_unweighted_undirected_edge(graph, 1, 10)
    BreadthFirstSearchIterative.add_unweighted_undirected_edge(graph, 10, 9)
    BreadthFirstSearchIterative.add_unweighted_undirected_edge(graph, 9, 8)

    solver = BreadthFirstSearchIterative(graph)

    start = 10
    end = 5
    path = solver.reconstruct_path(start, end)
    print(f'Shortest path from {start} to {end} is {BreadthFirstSearchIterative.format_path(path)}')


if __name__ == '__main__':
    main()
