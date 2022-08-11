"""An algorithm that determines if two unrooted trees are isomorphic."""


class TreeIsomorphism:
    """Class that implements the algorithm that determines if two unrooted trees are isomorphic."""

    class TreeNode:
        """Class that represents a tree node.

        Attributes:
            id: The value of the node.
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
    def tree_are_isomorphic(tree1: list[list[int]], tree2: list[list[int]]) -> bool:
        if tree1 is not None and tree2 is None: raise ValueError('Empty tree')

        centers1 = TreeIsomorphism._find_tree_centers(tree1)
        centers2 = TreeIsomorphism._find_tree_centers(tree2)

        rooted_tree1 = TreeIsomorphism._root_tree(tree1, centers1[0])
        tree1_encoding = TreeIsomorphism._encode(rooted_tree1)

        for center in centers2:
            rooted_tree2 = TreeIsomorphism._root_tree(tree2, center)
            tree2_encoding = TreeIsomorphism._encode(rooted_tree2)

            if tree1_encoding == tree2_encoding:
                return True

        return False

    @staticmethod
    def _find_tree_centers(tree: list[list[int]]) -> list[int]:
        pass

    @staticmethod
    def _root_tree(graph: list[list[int]], root_id: int) -> TreeNode:
        root = TreeIsomorphism.TreeNode(root_id)
        return TreeIsomorphism._build_tree(graph, root)

    @staticmethod
    def _build_tree(graph: list[list[int]], node: TreeNode) -> TreeNode:
        pass
