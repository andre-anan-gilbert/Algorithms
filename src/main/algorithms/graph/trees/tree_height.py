"""A tree height example."""


class TreeHeight:
    """Class that implements the tree height algorithm."""

    class TreeNode:
        """Class that represents a tree node.

        Attributes:
            value: The value of the node.
            left: The pointer to the left node.
            right: The pointer to the right node.
        """

        def __init__(self, value: int) -> None:
            self.value = value
            self.left = None
            self.right = None

    @staticmethod
    def tree_height1(node: TreeNode) -> int:
        if node is None: return -1
        return 1 + max(TreeHeight.tree_height1(node.left), TreeHeight.tree_height1(node.right))

    @staticmethod
    def tree_height2(node: TreeNode) -> int:
        if node is None: return -1
        if TreeHeight._is_leaf_node(node): return 0
        return 1 + max(TreeHeight.tree_height2(node.left), TreeHeight.tree_height2(node.right))

    @staticmethod
    def _is_leaf_node(node: TreeNode) -> bool:
        return node.left is None and node.right is None

    @staticmethod
    def make_tree() -> TreeNode:
        root = TreeHeight.TreeNode(0)

        node1 = TreeHeight.TreeNode(1)
        node2 = TreeHeight.TreeNode(2)
        root.left = node1
        root.right = node2

        node3 = TreeHeight.TreeNode(3)
        node4 = TreeHeight.TreeNode(4)
        node1.left = node3
        node1.right = node4

        node5 = TreeHeight.TreeNode(5)
        node6 = TreeHeight.TreeNode(6)
        node2.left = node5
        node2.right = node6

        node7 = TreeHeight.TreeNode(7)
        node8 = TreeHeight.TreeNode(8)
        node3.left = node7
        node3.right = node8

        return root


def main() -> None:
    tree_height1()
    tree_height2()


def tree_height1() -> None:
    print(f'Empty tree: {TreeHeight.tree_height1(None)}')
    print(f'Singelton height: {TreeHeight.tree_height1(TreeHeight.TreeNode(0))}')
    root = TreeHeight.make_tree()
    print(f'Tree height: {TreeHeight.tree_height1(root)}')


def tree_height2() -> None:
    print(f'Empty tree: {TreeHeight.tree_height2(None)}')
    print(f'Singelton height: {TreeHeight.tree_height2(TreeHeight.TreeNode(0))}')
    root = TreeHeight.make_tree()
    print(f'Tree height: {TreeHeight.tree_height2(root)}')


if __name__ == '__main__':
    main()
