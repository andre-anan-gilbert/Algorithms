"""An implementation of an interative depth first search."""


class DepthFirstSearchIterative:
    """Class that implements an iterative depth first search."""

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

    @staticmethod
    def dfs(graph: dict[int, list[_Edge]], start: int, n: int) -> int:
        """Performs an iterative depth first search.

        Args:
            graph: An adjacency list.
            start: The starting node.
            n: The number of nodes in the graph.

        Returns:
            The number of nodes traversed starting at some node.
        """
        count = 0
        visited = [False for _ in range(n)]
        stack = []

        stack.append(start)
        visited[start] = True

        while stack:
            node = stack.pop()
            count += 1
            edges = graph.get(node)

            if edges is not None:
                for edge in edges:
                    if not visited[edge.to]:
                        stack.append(edge.to)
                        visited[edge.to] = True

        return count

    @staticmethod
    def add_directed_edge(graph: dict[int, list[_Edge]], fr: int, to: int, cost: int) -> None:
        array = graph.get(fr)
        if array is None:
            array = []
            graph[fr] = array

        array.append(DepthFirstSearchIterative._Edge(fr, to, cost))


def main() -> None:
    num_nodes = 5
    graph = {}
    DepthFirstSearchIterative.add_directed_edge(graph, 0, 1, 4)
    DepthFirstSearchIterative.add_directed_edge(graph, 0, 2, 5)
    DepthFirstSearchIterative.add_directed_edge(graph, 1, 2, -2)
    DepthFirstSearchIterative.add_directed_edge(graph, 1, 3, 6)
    DepthFirstSearchIterative.add_directed_edge(graph, 2, 3, 1)
    DepthFirstSearchIterative.add_directed_edge(graph, 2, 2, 10)

    node_count = DepthFirstSearchIterative.dfs(graph, 0, num_nodes)
    print(f'DFS node cound starting at node 0: {node_count}.')
    if node_count != 4: print('Error with DFS.')

    node_count = DepthFirstSearchIterative.dfs(graph, 4, num_nodes)
    print(f'DFS node count starting at ndoe 4: {node_count}.')
    if node_count != 1: print('Error with DFS.')


if __name__ == '__main__':
    main()
