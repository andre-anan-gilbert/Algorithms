"""An implementation of a recursive breadth first search."""
from collections import deque


class BreadthFirstSearchRecursive:
    """Class that implements a recursive breadth first search."""
    DEPTH_TOKEN = -1

    @staticmethod
    def bfs(graph: list[list[int]], start: int, n: int) -> int:
        """Returns the distance to the furthest node from the starting node."""
        visited = [False for _ in range(n)]
        queue = deque()
        queue.append(start)
        queue.append(BreadthFirstSearchRecursive.DEPTH_TOKEN)
        return BreadthFirstSearchRecursive._bfs(visited, queue, graph)

    @staticmethod
    def _bfs(visited: list[bool], queue: deque[int], graph: list[list[int]]) -> int:
        """Performs a recursive breadth first search.

        Args:
            visited: A list of visited nodes.
            queue: A queue containing the nodes to visit.
            graph: An adjacency list.

        Returns:
            The distance to the furthest node.
        """
        at = queue.popleft()

        if at == BreadthFirstSearchRecursive.DEPTH_TOKEN:
            queue.append(BreadthFirstSearchRecursive.DEPTH_TOKEN)
            return 1

        if visited[at]: return 0

        visited[at] = True

        neighbours = graph[at]
        if neighbours is not None:
            for neighbour in neighbours:
                if not visited[neighbour]: queue.append(neighbour)

        depth = 0
        while True:
            if len(queue) == 1 and queue[0] == BreadthFirstSearchRecursive.DEPTH_TOKEN:
                break
            depth += BreadthFirstSearchRecursive._bfs(visited, queue, graph)
        return depth

    @staticmethod
    def add_directed_edge(graph: list[list[int]], fr: int, to: int) -> None:
        graph[fr].append(to)
        graph[to].append(fr)


def main() -> None:
    n = 14
    graph = [[] for _ in range(n)]

    BreadthFirstSearchRecursive.add_directed_edge(graph, 0, 1)
    BreadthFirstSearchRecursive.add_directed_edge(graph, 0, 2)
    BreadthFirstSearchRecursive.add_directed_edge(graph, 0, 3)
    BreadthFirstSearchRecursive.add_directed_edge(graph, 2, 9)
    BreadthFirstSearchRecursive.add_directed_edge(graph, 8, 2)
    BreadthFirstSearchRecursive.add_directed_edge(graph, 3, 4)
    BreadthFirstSearchRecursive.add_directed_edge(graph, 10, 11)
    BreadthFirstSearchRecursive.add_directed_edge(graph, 12, 13)
    BreadthFirstSearchRecursive.add_directed_edge(graph, 3, 5)
    BreadthFirstSearchRecursive.add_directed_edge(graph, 5, 7)
    BreadthFirstSearchRecursive.add_directed_edge(graph, 5, 6)
    BreadthFirstSearchRecursive.add_directed_edge(graph, 0, 10)
    BreadthFirstSearchRecursive.add_directed_edge(graph, 11, 12)

    print(f'BFS depth: {BreadthFirstSearchRecursive.bfs(graph, 12, n)}')


if __name__ == '__main__':
    main()
