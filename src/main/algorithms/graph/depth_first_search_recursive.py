"""An implementation of a recursive depth first search."""


class DepthFirstSearchRecursive:
    """Class that implements a recursive depth first search."""

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
    def dfs(at: int, visited: list[bool], graph: dict[int, list[_Edge]]) -> int:
        """Performs a recursive depth first search.

        Args:
            at: The current node we are visiting.
            visited: A list of visited nodes.
            graph: An adjacency list.

        Returns:
            The number of nodes traversed starting at some node.
        """
        if visited[at]: return 0

        visited[at] = True
        count = 1

        edges = graph.get(at)
        if edges is not None:
            for edge in edges:
                count += DepthFirstSearchRecursive.dfs(edge.to, visited, graph)

        return count

    @staticmethod
    def add_directed_edge(graph: dict[int, list[_Edge]], fr: int, to: int, cost: int) -> None:
        array = graph.get(fr)
        if array is None:
            array = []
            graph[fr] = array

        array.append(DepthFirstSearchRecursive._Edge(fr, to, cost))


def main() -> None:
    num_nodes = 5
    graph = {}
    DepthFirstSearchRecursive.add_directed_edge(graph, 0, 1, 4)
    DepthFirstSearchRecursive.add_directed_edge(graph, 0, 2, 5)
    DepthFirstSearchRecursive.add_directed_edge(graph, 1, 2, -2)
    DepthFirstSearchRecursive.add_directed_edge(graph, 1, 3, 6)
    DepthFirstSearchRecursive.add_directed_edge(graph, 2, 3, 1)
    DepthFirstSearchRecursive.add_directed_edge(graph, 2, 2, 10)

    node_count = DepthFirstSearchRecursive.dfs(0, [False for _ in range(num_nodes)], graph)
    print(f'DFS node cound starting at node 0: {node_count}.')
    if node_count != 4: print('Error with DFS.')

    node_count = DepthFirstSearchRecursive.dfs(4, [False for _ in range(num_nodes)], graph)
    print(f'DFS node count starting at ndoe 4: {node_count}.')
    if node_count != 1: print('Error with DFS.')


if __name__ == '__main__':
    main()
