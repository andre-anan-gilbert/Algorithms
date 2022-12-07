"""A tree sum example."""


class TreeSum:
    """Class that implements the tree sum algorithm."""

    class TreeNode:
        """Class that represents a tree node.

        Attributes:
            value: The value of the node.
            children: A list of children of the node.
        """

        def __init__(self, value: int) -> None:
            self.value = value
            self.children = []

        def add_child(self, *nodes) -> None:
            for node in nodes:
                self.children.append(node)

    @staticmethod
    def tree_sum(node: TreeNode) -> int:
        if node is None: return 0

        total = 0
        for child in node.children:
            total += TreeSum.tree_sum(child)
        total += node.value
        return total

    @staticmethod
    def make_tree() -> TreeNode:
        root = TreeSum.TreeNode(5)

        node4 = TreeSum.TreeNode(4)
        node3 = TreeSum.TreeNode(3)
        root.add_child(node4, node3)

        node1 = TreeSum.TreeNode(1)
        nodem6 = TreeSum.TreeNode(-6)
        node4.add_child(node1, nodem6)

        node0 = TreeSum.TreeNode(0)
        node7 = TreeSum.TreeNode(7)
        nodem4 = TreeSum.TreeNode(-4)
        nodem4.add_child(node0, node7, nodem4)

        node2 = TreeSum.TreeNode(2)
        node9 = TreeSum.TreeNode(9)
        node1.add_child(node2, node9)

        node8 = TreeSum.TreeNode(8)
        node7.add_child(node8)

        return root


def main() -> None:
    tree = TreeSum.make_tree()
    print(f'Tree sum: {TreeSum.tree_sum(tree)}')


if __name__ == '__main__':
    main()
