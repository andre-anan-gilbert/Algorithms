"""An example of turning a graph with undirected edges into a rooted tree."""
from collections import deque


class RootingTree:
    """Class that implements rooting a tree."""

    class TreeNode:
        """Class that represents a tree node.

        Attributes:
            root_id: The value of the node.
            parent: The parent of the node.
            children: The children of the node.
        """

        def __init__(self, root_id: int, parent=None) -> None:
            self.id = root_id
            self.parent = parent
            self.children = []

        def add_children(self, *nodes) -> None:
            for node in nodes:
                self.children.append(node)

        def __repr__(self) -> str:
            return str(self.id)

    @staticmethod
    def root_tree(graph: list[list[int]], root_id: int) -> TreeNode:
        root = RootingTree.TreeNode(root_id)
        return RootingTree.build_tree(graph, root)

    @staticmethod
    def build_tree(graph: list[list[int]], node: TreeNode) -> TreeNode:
        """Builds the tree using depth first search."""
        for child_id in graph[node.id]:
            if node.parent is not None and child_id == node.parent.id:
                continue

            child = RootingTree.TreeNode(child_id, node)
            node.add_children(child)

            RootingTree.build_tree(graph, child)

        return node

    @staticmethod
    def create_graph(n: int) -> list[list[int]]:
        """Returns a graph as an adjacency list."""
        return [deque() for _ in range(n)]

    @staticmethod
    def add_undirected_edge(graph: list[list[int]], fr: int, to: int) -> None:
        graph[fr].append(to)
        graph[to].append(fr)


def main() -> None:
    graph = RootingTree.create_graph(9)
    RootingTree.add_undirected_edge(graph, 0, 1)
    RootingTree.add_undirected_edge(graph, 2, 1)
    RootingTree.add_undirected_edge(graph, 2, 3)
    RootingTree.add_undirected_edge(graph, 3, 4)
    RootingTree.add_undirected_edge(graph, 5, 3)
    RootingTree.add_undirected_edge(graph, 2, 6)
    RootingTree.add_undirected_edge(graph, 6, 7)
    RootingTree.add_undirected_edge(graph, 6, 8)

    root = RootingTree.root_tree(graph, 6)

    print(graph)

    # 0: [6]
    print(root)

    # 1: [2, 7, 8]
    print(root.children)

    # 2: [1, 3]
    print(root.children[0].children)

    # 3: [0], [4, 5]
    print(f'{root.children[0].children[0].children},', root.children[0].children[1].children)

    root = RootingTree.root_tree(graph, 3)

    # 0: [3]
    print(root)

    # 1: [2, 4, 5]
    print(root.children)

    # 2: [1, 6]
    print(root.children[0].children)

    # 3: [0], [7, 8]
    print(f'{root.children[0].children[0].children},', root.children[0].children[1].children)


if __name__ == '__main__':
    main()
