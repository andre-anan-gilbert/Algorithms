"""Tests the fenwick tree implementation."""
import random
import unittest
from main.data_structures.fenwick_tree.fenwick_tree import FenwickTree


class TestFenwickTree(unittest.TestCase):
    """Class that tests the fenwick tree implementation."""

    def setUp(self) -> None:
        self._min_rand_num = -1000
        self._max_rand_num = +1000

        self._test_sz = 1000
        self._loops = 1000

        self._unused_val = self.random_value()

    def test_interval_sum_positive_values(self) -> None:
        arr = [self._unused_val, 1, 2, 3, 4, 5, 6]
        fenwick_tree = FenwickTree(values=arr)

        self.assertEqual(fenwick_tree.sum(1, 6), 21)
        self.assertEqual(fenwick_tree.sum(1, 5), 15)
        self.assertEqual(fenwick_tree.sum(1, 4), 10)
        self.assertEqual(fenwick_tree.sum(1, 3), 6)
        self.assertEqual(fenwick_tree.sum(1, 2), 3)
        self.assertEqual(fenwick_tree.sum(1, 1), 1)

        self.assertEqual(fenwick_tree.sum(3, 4), 7)
        self.assertEqual(fenwick_tree.sum(2, 6), 20)
        self.assertEqual(fenwick_tree.sum(4, 5), 9)
        self.assertEqual(fenwick_tree.sum(6, 6), 6)
        self.assertEqual(fenwick_tree.sum(5, 5), 5)
        self.assertEqual(fenwick_tree.sum(4, 4), 4)
        self.assertEqual(fenwick_tree.sum(3, 3), 3)
        self.assertEqual(fenwick_tree.sum(2, 2), 2)
        self.assertEqual(fenwick_tree.sum(1, 1), 1)

    def test_interval_sum_negative_values(self) -> None:
        arr = [self._unused_val, -1, -2, -3, -4, -5, -6]
        fenwick_tree = FenwickTree(values=arr)

        self.assertEqual(fenwick_tree.sum(1, 6), -21)
        self.assertEqual(fenwick_tree.sum(1, 5), -15)
        self.assertEqual(fenwick_tree.sum(1, 4), -10)
        self.assertEqual(fenwick_tree.sum(1, 3), -6)
        self.assertEqual(fenwick_tree.sum(1, 2), -3)
        self.assertEqual(fenwick_tree.sum(1, 1), -1)

        self.assertEqual(fenwick_tree.sum(6, 6), -6)
        self.assertEqual(fenwick_tree.sum(5, 5), -5)
        self.assertEqual(fenwick_tree.sum(4, 4), -4)
        self.assertEqual(fenwick_tree.sum(3, 3), -3)
        self.assertEqual(fenwick_tree.sum(2, 2), -2)
        self.assertEqual(fenwick_tree.sum(1, 1), -1)

    def test_interval_sum_negative_values2(self) -> None:
        arr = [self._unused_val, -76871, -164790]
        fenwick_tree = FenwickTree(values=arr)

        for _ in range(self._loops):
            self.assertEqual(fenwick_tree.sum(1, 1), -76871)
            self.assertEqual(fenwick_tree.sum(1, 1), -76871)
            self.assertEqual(fenwick_tree.sum(1, 2), -241661)
            self.assertEqual(fenwick_tree.sum(1, 2), -241661)
            self.assertEqual(fenwick_tree.sum(1, 2), -241661)
            self.assertEqual(fenwick_tree.sum(2, 2), -164790)
            self.assertEqual(fenwick_tree.sum(2, 2), -164790)
            self.assertEqual(fenwick_tree.sum(2, 2), -164790)

    def test_randomized_static_range_queries(self) -> None:
        for i in range(1, self._loops + 1):
            rand_list = self.generate_random_list(i)
            fenwick_tree = FenwickTree(values=rand_list)

            for _ in range(self._loops // 10):
                self.do_random_range_query(rand_list, fenwick_tree)

    def do_random_range_query(self, array: list[int], fenwick_tree: FenwickTree) -> None:
        range_sum = 0
        n = len(array) - 1

        low = self.low_bound(n)
        high = self.high_bound(low, n)

        for k in range(low, high + 1):
            range_sum += array[k]

        self.assertEqual(fenwick_tree.sum(low, high), range_sum)

    def test_randomized_sum_queries(self) -> None:
        for n in range(2, self._loops + 1):
            rand_list = self.generate_random_list(n)
            fenwick_tree = FenwickTree(values=rand_list)

            for _ in range(self._loops // 10):
                index = 1 + int(random.random() * n)
                rand_val = self.random_value()

                rand_list[index] += rand_val
                fenwick_tree.add(index, rand_val)

                self.do_random_range_query(rand_list, fenwick_tree)

    def test_reusebility(self) -> None:
        size = 1000
        fenwick_tree = FenwickTree(size)
        array = [0 for _ in range(size + 1)]

        for _ in range(self._loops):
            for i in range(1, size + 1):
                val = self.random_value()
                fenwick_tree.set(i, val)
                array[i] = val

            self.do_random_range_query(array, fenwick_tree)

    def low_bound(self, n: int) -> int:
        return 1 + int(random.random() * n)

    def high_bound(self, low: int, n: int) -> int:
        return min(n, low + int(random.random() * n))

    def random_value(self) -> int:
        return int(random.random() * self._max_rand_num * 2) + self._min_rand_num

    def generate_random_list(self, size: int) -> list[int]:
        array = list(range(size + 1))
        for i in range(1, size + 1):
            array[i] = self.random_value()

        return array
