"""Tests the binary search tree implementation."""
import random
import unittest
from collections import deque
from main.data_structures.binary_search_tree.binary_search_tree import BinarySearchTree, TreeTraversalOrder


class TreeNode:
    """Class that represents a tree node."""

    def __init__(self, data: int, left, right) -> None:
        self.data = data
        self.left = left
        self.right = right

    @staticmethod
    def add(node, data: int):
        if node is None:
            node = TreeNode(data, None, None)
        else:
            if data < node.data:
                node.left = TreeNode.add(node.left, data)
            else:
                node.right = TreeNode.add(node.right, data)

        return node


def pre_order(array: list[int], node: TreeNode) -> None:
    if node is None: return

    array.append(node.data)
    if node.left is not None: pre_order(array, node.left)
    if node.right is not None: pre_order(array, node.right)


def in_order(array: list[int], node: TreeNode) -> None:
    if node is None: return

    if node.left is not None: in_order(array, node.left)
    array.append(node.data)
    if node.right is not None: in_order(array, node.right)


def post_order(array: list[int], node: TreeNode) -> None:
    if node is None: return

    if node.left is not None: post_order(array, node.left)
    if node.right is not None: post_order(array, node.right)
    array.append(node.data)


def level_order(array: list[int], node: TreeNode) -> None:
    q = deque()
    if node is not None: q.append(node)

    while q:
        node = q.popleft()
        array.append(node.data)
        if node.left is not None: q.append(node.left)
        if node.right is not None: q.append(node.right)


class TestBinarySearchTree(unittest.TestCase):
    """Class that tests the binary search tree implementation."""

    def setUp(self) -> None:
        self._loops = 100
        self._binary_search_tree = BinarySearchTree()

    def test_empty(self) -> None:
        self.assertTrue(self._binary_search_tree.is_empty())
        self._binary_search_tree.add('A')
        self.assertFalse(self._binary_search_tree.is_empty())

    def test_size(self) -> None:
        self.assertEqual(self._binary_search_tree.size(), 0)
        self._binary_search_tree.add('A')
        self.assertEqual(self._binary_search_tree.size(), 1)

    def test_height(self) -> None:
        self.assertEqual(self._binary_search_tree.height(), 0)

        self._binary_search_tree.add('M')
        self.assertEqual(self._binary_search_tree.height(), 1)

        self._binary_search_tree.add('J')
        self.assertEqual(self._binary_search_tree.height(), 2)
        self._binary_search_tree.add('S')
        self.assertEqual(self._binary_search_tree.height(), 2)

        self._binary_search_tree.add('B')
        self.assertEqual(self._binary_search_tree.height(), 3)
        self._binary_search_tree.add('N')
        self.assertEqual(self._binary_search_tree.height(), 3)
        self._binary_search_tree.add('Z')
        self.assertEqual(self._binary_search_tree.height(), 3)

        self._binary_search_tree.add('A')
        self.assertEqual(self._binary_search_tree.height(), 4)

    def test_add(self) -> None:
        self.assertTrue(self._binary_search_tree.add('A'))
        self.assertFalse(self._binary_search_tree.add('A'))
        self.assertTrue(self._binary_search_tree.add('B'))

    def test_remove(self) -> None:
        self._binary_search_tree.add('A')
        self.assertEqual(self._binary_search_tree.size(), 1)
        self.assertFalse(self._binary_search_tree.remove('B'))
        self.assertEqual(self._binary_search_tree.size(), 1)

        self._binary_search_tree.add('B')
        self.assertEqual(self._binary_search_tree.size(), 2)
        self.assertTrue(self._binary_search_tree.remove('B'))
        self.assertEqual(self._binary_search_tree.size(), 1)
        self.assertEqual(self._binary_search_tree.height(), 1)

        self.assertTrue(self._binary_search_tree.remove('A'))
        self.assertEqual(self._binary_search_tree.size(), 0)
        self.assertEqual(self._binary_search_tree.height(), 0)

    def test_contains(self) -> None:
        self._binary_search_tree.add('A')
        self._binary_search_tree.add('B')
        self._binary_search_tree.add('C')

        self.assertFalse(self._binary_search_tree.contains('D'))
        self.assertTrue(self._binary_search_tree.contains('B'))
        self.assertTrue(self._binary_search_tree.contains('A'))
        self.assertTrue(self._binary_search_tree.contains('C'))

    def test_pre_order_concurrent_modification_error(self) -> None:
        self._binary_search_tree.add(1)
        self._binary_search_tree.add(2)
        self._binary_search_tree.add(3)
        with self.assertRaises(Exception):
            for _ in self._binary_search_tree.traverse(TreeTraversalOrder.PRE_ORDER):
                self._binary_search_tree.remove(2)

    def test_in_order_concurrent_modification_error(self) -> None:
        self._binary_search_tree.add(1)
        self._binary_search_tree.add(2)
        self._binary_search_tree.add(3)
        with self.assertRaises(Exception):
            for _ in self._binary_search_tree.traverse(TreeTraversalOrder.IN_ORDER):
                self._binary_search_tree.remove(2)

    def test_post_order_concurrent_modification_error(self) -> None:
        self._binary_search_tree.add(1)
        self._binary_search_tree.add(2)
        self._binary_search_tree.add(3)
        with self.assertRaises(Exception):
            for _ in self._binary_search_tree.traverse(TreeTraversalOrder.POST_ORDER):
                self._binary_search_tree.remove(2)

    def test_level_order_concurrent_modification_error(self) -> None:
        self._binary_search_tree.add(1)
        self._binary_search_tree.add(2)
        self._binary_search_tree.add(3)

        with self.assertRaises(Exception):
            for _ in self._binary_search_tree.traverse(TreeTraversalOrder.LEVEL_ORDER):
                self._binary_search_tree.remove(2)

    def test_randomized_removing(self) -> None:
        for i in range(0, self._loops):
            size = i
            array = self._generate_random_list(size)
            for value in array:
                self._binary_search_tree.add(value)

            random.shuffle(array)

            for j in range(size):
                value = array[j]

                self.assertTrue(self._binary_search_tree.remove(value))
                self.assertFalse(self._binary_search_tree.contains(value))
                self.assertEqual(self._binary_search_tree.size(), size - j - 1)

            self.assertTrue(self._binary_search_tree.is_empty())

    def validate_tree_traversal(self, trav_order: TreeTraversalOrder, array: list[int]) -> None:
        output = []
        expected = []

        test_tree = None
        tree = BinarySearchTree()

        # Construct Binary Tree and test tree
        for value in array:
            test_tree = TreeNode.add(test_tree, value)
            tree.add(value)

        # Generate the expected output for the particular traversal
        if trav_order is TreeTraversalOrder.PRE_ORDER:
            pre_order(expected, test_tree)
        elif trav_order is TreeTraversalOrder.IN_ORDER:
            in_order(expected, test_tree)
        elif trav_order is TreeTraversalOrder.POST_ORDER:
            post_order(expected, test_tree)
        elif trav_order is TreeTraversalOrder.LEVEL_ORDER:
            level_order(expected, test_tree)

        # Get traversal output
        for i in tree.traverse(trav_order):
            output.append(i)

        if len(output) != len(expected):
            return False

        # Compare output to expected
        if expected != output:
            return False

        return True

    def test_pre_order_traversal(self) -> None:
        for i in range(1, self._loops):
            array = self._generate_random_list(i)
            self.assertTrue(self.validate_tree_traversal(TreeTraversalOrder.PRE_ORDER, array))

    def test_in_order_traversal(self) -> None:
        for i in range(1, self._loops):
            array = self._generate_random_list(i)
            self.assertTrue(self.validate_tree_traversal(TreeTraversalOrder.IN_ORDER, array))

    def test_post_order_traversal(self) -> None:
        for i in range(1, self._loops):
            array = self._generate_random_list(i)
            self.assertTrue(self.validate_tree_traversal(TreeTraversalOrder.POST_ORDER, array))

    def test_level_order_traversal(self) -> None:
        for i in range(1, self._loops):
            array = self._generate_random_list(i)
            self.assertTrue(self.validate_tree_traversal(TreeTraversalOrder.LEVEL_ORDER, array))

    def _generate_random_list(self, size: int) -> list[int]:
        array = list(range(size))
        random.shuffle(array)
        return array
