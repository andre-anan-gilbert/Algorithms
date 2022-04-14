"""Tests the union find/disjoint set implementation."""
import unittest
from main.data_structures.union_find.union_find import UnionFind


class TestUnionFind(unittest.TestCase):
    """Class thats tests the union find implementation."""

    def setUp(self) -> None:
        self._union_find = UnionFind(5)

    def test_num_components(self) -> None:
        self._union_find.unify(0, 1)
        self.assertEqual(self._union_find.components(), 4)

        self._union_find.unify(1, 0)
        self.assertEqual(self._union_find.components(), 4)

        self._union_find.unify(1, 2)
        self.assertEqual(self._union_find.components(), 3)

        self._union_find.unify(0, 2)
        self.assertEqual(self._union_find.components(), 3)

        self._union_find.unify(2, 1)
        self.assertEqual(self._union_find.components(), 3)

        self._union_find.unify(3, 4)
        self.assertEqual(self._union_find.components(), 2)

        self._union_find.unify(4, 3)
        self.assertEqual(self._union_find.components(), 2)

        self._union_find.unify(1, 3)
        self.assertEqual(self._union_find.components(), 1)

        self._union_find.unify(4, 0)
        self.assertEqual(self._union_find.components(), 1)

    def test_component_size(self) -> None:
        self.assertEqual(self._union_find.component_size(0), 1)
        self.assertEqual(self._union_find.component_size(1), 1)
        self.assertEqual(self._union_find.component_size(2), 1)
        self.assertEqual(self._union_find.component_size(3), 1)
        self.assertEqual(self._union_find.component_size(4), 1)

        self._union_find.unify(0, 1)
        self.assertEqual(self._union_find.component_size(0), 2)
        self.assertEqual(self._union_find.component_size(1), 2)
        self.assertEqual(self._union_find.component_size(2), 1)
        self.assertEqual(self._union_find.component_size(3), 1)
        self.assertEqual(self._union_find.component_size(4), 1)

        self._union_find.unify(1, 0)
        self.assertEqual(self._union_find.component_size(0), 2)
        self.assertEqual(self._union_find.component_size(1), 2)
        self.assertEqual(self._union_find.component_size(2), 1)
        self.assertEqual(self._union_find.component_size(3), 1)
        self.assertEqual(self._union_find.component_size(4), 1)

        self._union_find.unify(1, 2)
        self.assertEqual(self._union_find.component_size(0), 3)
        self.assertEqual(self._union_find.component_size(1), 3)
        self.assertEqual(self._union_find.component_size(2), 3)
        self.assertEqual(self._union_find.component_size(3), 1)
        self.assertEqual(self._union_find.component_size(4), 1)

        self._union_find.unify(0, 2)
        self.assertEqual(self._union_find.component_size(0), 3)
        self.assertEqual(self._union_find.component_size(1), 3)
        self.assertEqual(self._union_find.component_size(2), 3)
        self.assertEqual(self._union_find.component_size(3), 1)
        self.assertEqual(self._union_find.component_size(4), 1)

        self._union_find.unify(2, 1)
        self.assertEqual(self._union_find.component_size(0), 3)
        self.assertEqual(self._union_find.component_size(1), 3)
        self.assertEqual(self._union_find.component_size(2), 3)
        self.assertEqual(self._union_find.component_size(3), 1)
        self.assertEqual(self._union_find.component_size(4), 1)

        self._union_find.unify(3, 4)
        self.assertEqual(self._union_find.component_size(0), 3)
        self.assertEqual(self._union_find.component_size(1), 3)
        self.assertEqual(self._union_find.component_size(2), 3)
        self.assertEqual(self._union_find.component_size(3), 2)
        self.assertEqual(self._union_find.component_size(4), 2)

        self._union_find.unify(4, 3)
        self.assertEqual(self._union_find.component_size(0), 3)
        self.assertEqual(self._union_find.component_size(1), 3)
        self.assertEqual(self._union_find.component_size(2), 3)
        self.assertEqual(self._union_find.component_size(3), 2)
        self.assertEqual(self._union_find.component_size(4), 2)

        self._union_find.unify(1, 3)
        self.assertEqual(self._union_find.component_size(0), 5)
        self.assertEqual(self._union_find.component_size(1), 5)
        self.assertEqual(self._union_find.component_size(2), 5)
        self.assertEqual(self._union_find.component_size(3), 5)
        self.assertEqual(self._union_find.component_size(4), 5)

        self._union_find.unify(4, 0)
        self.assertEqual(self._union_find.component_size(0), 5)
        self.assertEqual(self._union_find.component_size(1), 5)
        self.assertEqual(self._union_find.component_size(2), 5)
        self.assertEqual(self._union_find.component_size(3), 5)
        self.assertEqual(self._union_find.component_size(4), 5)

    def test_connectivity(self) -> None:
        size = 5

        for i in range(size):
            self.assertTrue(self._union_find.connected(i, i))

        self._union_find.unify(0, 2)

        self.assertTrue(self._union_find.connected(0, 2))
        self.assertTrue(self._union_find.connected(2, 0))

        self.assertFalse(self._union_find.connected(0, 1))
        self.assertFalse(self._union_find.connected(3, 1))
        self.assertFalse(self._union_find.connected(1, 4))

        for i in range(size):
            self.assertTrue(self._union_find.connected(i, i))

        self._union_find.unify(3, 1)

        self.assertTrue(self._union_find.connected(0, 2))
        self.assertTrue(self._union_find.connected(2, 0))
        self.assertTrue(self._union_find.connected(1, 3))
        self.assertTrue(self._union_find.connected(3, 1))

        self.assertFalse(self._union_find.connected(0, 1))
        self.assertFalse(self._union_find.connected(1, 2))
        self.assertFalse(self._union_find.connected(2, 3))
        self.assertFalse(self._union_find.connected(1, 0))
        self.assertFalse(self._union_find.connected(2, 1))
        self.assertFalse(self._union_find.connected(3, 2))
        self.assertFalse(self._union_find.connected(1, 4))

        for i in range(size):
            self.assertTrue(self._union_find.connected(i, i))

        self._union_find.unify(1, 2)
        self._union_find.unify(3, 4)

        for i in range(size):
            for j in range(size):
                self.assertTrue(self._union_find.connected(i, j))

    def test_size(self) -> None:
        self.assertEqual(self._union_find.size(), 5)
        self._union_find.unify(0, 1)
        self._union_find.find(3)
        self.assertEqual(self._union_find.size(), 5)
        self._union_find.unify(1, 2)
        self.assertEqual(self._union_find.size(), 5)
        self._union_find.unify(0, 2)
        self._union_find.find(1)
        self.assertEqual(self._union_find.size(), 5)
        self._union_find.unify(2, 1)
        self.assertEqual(self._union_find.size(), 5)
        self._union_find.unify(3, 4)
        self._union_find.find(0)
        self.assertEqual(self._union_find.size(), 5)
        self._union_find.unify(4, 3)
        self._union_find.find(3)
        self.assertEqual(self._union_find.size(), 5)
        self._union_find.unify(1, 3)
        self._union_find.find(2)
        self.assertEqual(self._union_find.size(), 5)
        self._union_find.unify(4, 0)
        self.assertEqual(self._union_find.size(), 5)

    def test_bad_init(self) -> None:
        for _ in range(-2, 1):
            self.assertRaises(Exception, UnionFind)
