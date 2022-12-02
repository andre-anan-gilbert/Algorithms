"""An implementation of a binary search tree."""
from collections import deque
from enum import Enum, auto
from typing import Generator, Generic, TypeVar


class TreeTraversalOrder(Enum):
    PRE_ORDER = auto()
    IN_ORDER = auto()
    POST_ORDER = auto()
    LEVEL_ORDER = auto()


T = TypeVar('T')


class BinarySearchTree(Generic[T]):
    """Class that represents a binary search tree.

    Attributes:
        _node_count: The number of nodes in the tree.
        _root: The root of the tree.
    """

    def __init__(self) -> None:
        self._node_count = 0
        self._root = None

    class _Node:
        """Class that represents a node in a binary search tree.

        Attributes:
            data: The node data.
            left: The pointer to the left node.
            right: The pointer to the right node.
        """

        def __init__(self, data: T, left, right) -> None:
            self.data = data
            self.left = left
            self.right = right

    def size(self) -> int:
        """Return the size of the tree."""
        return self._node_count

    def is_empty(self) -> bool:
        """Checks if the tree is empty."""
        return self.size() == 0

    def add(self, elem: T) -> bool:
        """Adds an element to the tree."""
        if self.contains(elem):
            return False
        else:
            self._root = self._add(self._root, elem)
            self._node_count += 1
            return True

    def _add(self, node: _Node, elem: T) -> _Node:
        """Adds a node to the tree."""
        if node is None:
            node = self._Node(elem, None, None)
        else:
            if elem < node.data:
                node.left = self._add(node.left, elem)
            else:
                node.right = self._add(node.right, elem)
        return node

    def remove(self, elem: T) -> bool:
        """Removes a node from the tree."""
        if self.contains(elem):
            self._root = self._remove(self._root, elem)
            self._node_count -= 1
            return True
        return False

    def _remove(self, node: _Node, elem: T) -> bool:
        """Removes a node from the tree."""
        if node is None: return

        if elem == node.data:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                tmp = self._find_min(node.right)
                node.data = tmp.data
                node.right = self._remove(node.right, tmp.data)

        cmp = elem < node.data
        if cmp:
            node.left = self._remove(node.left, elem)
        else:
            node.right = self._remove(node.right, elem)
        return node

    def _find_min(self, node: _Node) -> _Node:
        """Returns the smallest node in the right subtree."""
        while node.left is not None:
            node = node.left
        return node

    def contains(self, elem: T) -> bool:
        """Checks if the tree contains the element."""
        return self._contains(self._root, elem)

    def _contains(self, node: _Node, elem: T) -> bool:
        """Checks if the node with the element exists."""
        if node is None: return False
        if elem == node.data: return True

        cmp = elem < node.data
        if cmp:
            return self._contains(node.left, elem)
        elif not cmp:
            return self._contains(node.right, elem)
        else:
            return True

    def height(self) -> int:
        """Returns the height of the tree."""
        return self._height(self._root)

    def _height(self, node: _Node) -> int:
        """Computes the height of the tree."""
        if node is None: return 0
        return max(self._height(node.left), self._height(node.right)) + 1

    def traverse(self, order: TreeTraversalOrder) -> Generator:
        """Returns a generator for a given tree traversal order."""
        if order == TreeTraversalOrder.PRE_ORDER:
            return self._pre_order_traversal()
        elif order == TreeTraversalOrder.IN_ORDER:
            return self._in_order_traversal()
        elif order == TreeTraversalOrder.POST_ORDER:
            return self._post_order_travesal()
        elif order == TreeTraversalOrder.LEVEL_ORDER:
            return self._level_order_traversal()
        else:
            return

    def _pre_order_traversal(self) -> Generator:
        if self._root is None: return

        expected_node_count = self._node_count
        stack = deque()
        stack.append(self._root)

        while self._root is not None and stack:
            if expected_node_count != self._node_count:
                raise RuntimeError()

            node = stack.pop()
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)

            yield node.data

    def _in_order_traversal(self) -> Generator:
        if self._root is None: return

        expected_node_count = self._node_count
        stack = deque()
        stack.append(self._root)
        trav = self._root

        while self._root is not None and stack:
            if expected_node_count != self._node_count:
                raise RuntimeError()

            # Dig left
            while trav is not None and trav.left is not None:
                stack.append(trav.left)
                trav = trav.left

            node = stack.pop()

            # Try moving down right once
            if node.right is not None:
                stack.append(node.right)
                trav = node.right

            yield node.data

    def _post_order_travesal(self) -> Generator:
        if self._root is None: return

        expected_node_count = self._node_count
        stack1 = deque()
        stack1.append(self._root)
        stack2 = deque()

        while stack1:
            node = stack1.pop()
            if node is not None:
                stack2.append(node)
                if node.left is not None:
                    stack1.append(node.left)
                if node.right is not None:
                    stack1.append(node.right)

        while self._root is not None and stack2:
            if expected_node_count != self._node_count:
                raise RuntimeError()

            node = stack2.pop()

            yield node.data

    def _level_order_traversal(self) -> Generator:
        if self._root is None: return

        expected_node_count = self._node_count
        queue = deque()
        queue.append(self._root)

        while self._root is not None and queue:
            if expected_node_count != self._node_count:
                raise RuntimeError()

            node = queue.popleft()

            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

            yield node.data


def main() -> None:
    binary_search_tree = BinarySearchTree()
    print(binary_search_tree.is_empty())
    binary_search_tree.add(1)
    binary_search_tree.add(2)
    binary_search_tree.add(3)
    binary_search_tree.add(4)
    binary_search_tree.add(5)
    binary_search_tree.add(6)
    print(binary_search_tree.size())
    print(binary_search_tree.is_empty())
    print(binary_search_tree.height())
    for node in binary_search_tree.traverse(TreeTraversalOrder.PRE_ORDER):
        print(node)

    print(binary_search_tree.contains(6))
    binary_search_tree.remove(6)
    print(binary_search_tree.contains(6))


if __name__ == '__main__':
    main()
