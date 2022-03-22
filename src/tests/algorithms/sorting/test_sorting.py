"""Tests the sorting implementations."""
import copy
import random
import unittest
from enum import Enum, auto
from main.algorithms.sorting.bubble_sort import BubbleSort
from main.algorithms.sorting.heapsort import Heapsort
from main.algorithms.sorting.quick_sort import QuickSort
from main.algorithms.sorting.insertion_sort import InsertionSort
from main.algorithms.sorting.selection_sort import SelectionSort


class SortingAlgorithm(Enum):
    BUBBLE_SORT = auto()
    HEAP_SORT = auto()
    QUICK_SORT = auto()
    INSERTION_SORT = auto()
    SELECTION_SORT = auto()


class TestSorting(unittest.TestCase):
    """Class that tests sorting algorithms."""

    def setUp(self) -> None:
        self._loops = 100
        self._algorithms = {
            SortingAlgorithm.BUBBLE_SORT: BubbleSort,
            SortingAlgorithm.HEAP_SORT: Heapsort,
            SortingAlgorithm.QUICK_SORT: QuickSort,
            SortingAlgorithm.INSERTION_SORT: InsertionSort,
            SortingAlgorithm.SELECTION_SORT: SelectionSort,
        }

    def test_small_positive_integers(self) -> None:
        for size in range(0, self._loops):
            for algorithm in self._algorithms:
                sorter = self._algorithms.get(algorithm)()
                values = self._generate_random_list(size, 0, 51)
                cpy = copy.deepcopy(values)

                values.sort()
                sorter.sort(cpy)

                self.assertEqual(values, cpy)

    def test_small_negative_integers(self) -> None:
        for size in range(0, self._loops):
            for algorithm in self._algorithms:
                sorter = self._algorithms.get(algorithm)()
                values = self._generate_random_list(size, -50, 51)
                cpy = copy.deepcopy(values)

                values.sort()
                sorter.sort(cpy)

                self.assertEqual(values, cpy)

    def _generate_random_list(self, size: int, low: int, high: int) -> list[int]:
        return [random.randint(low, high) for _ in range(0, size)]
