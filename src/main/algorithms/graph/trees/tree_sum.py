"""A tree sum example."""


class TreeSum:
    """Class that implements the tree sum algorithm."""

    class _TreeNode:
        """Class that represents a tree node.

        Attributes:
            value: The value of the node.
            children: A list of children of the node.
        """

        def __init__(self, value: int) -> None:
            self.value = value
            self.children = []

        def get_value(self) -> int:
            return self.value

        def get_children(self) -> list:
            return self.children

        def add_child(self, *nodes) -> None:
            for node in nodes:
                self.children.append(node)

    @staticmethod
    def tree_sum(node: _TreeNode) -> int:
        if node is None: return 0

        total = 0
        for child in node.get_children():
            total += TreeSum.tree_sum(child)

        total += node.get_value()
        return total

    @staticmethod
    def make_tree() -> _TreeNode:
        root = TreeSum._TreeNode(5)

        node4 = TreeSum._TreeNode(4)
        node3 = TreeSum._TreeNode(3)
        root.add_child(node4, node3)

        node1 = TreeSum._TreeNode(1)
        nodem6 = TreeSum._TreeNode(-6)
        node4.add_child(node1, nodem6)

        node0 = TreeSum._TreeNode(0)
        node7 = TreeSum._TreeNode(7)
        nodem4 = TreeSum._TreeNode(-4)
        nodem4.add_child(node0, node7, nodem4)

        node2 = TreeSum._TreeNode(2)
        node9 = TreeSum._TreeNode(9)
        node1.add_child(node2, node9)

        node8 = TreeSum._TreeNode(8)
        node7.add_child(node8)

        return root


def main() -> None:
    tree = TreeSum.make_tree()
    print(f'Tree sum: {TreeSum.tree_sum(tree)}')


if __name__ == '__main__':
    main()
