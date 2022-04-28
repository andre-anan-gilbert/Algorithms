"""An implementation of a fenwick tree."""
import copy
import random


class FenwickTree:
    """Class that represents a fenwick tree.

    Attributes:
        _n: The size of the array holding the tree values.
        _tree: The array containing the range values.
    """

    def __init__(self, size: int = None, values: list[int] = None) -> None:
        """Inits the fenwick tree.

        Args:
            size: Create an empty tree with 'size'.
            values: Construct a tree with an initial set of values.
        """
        if size is not None and values is None:
            self._n = size + 1
            self._tree = [0 for _ in range(size + 1)]
        else:
            if not values: raise ValueError('Values array cannot be empty.')

            self._n = len(values)
            values[0] = 0

            self._tree = copy.deepcopy(values)

            for i in range(1, self._n):
                parent = i + self._lsb(i)
                if parent < self._n: self._tree[parent] += self._tree[i]

    def _lsb(self, i: int) -> int:
        """Finds the least significant bit."""
        return i & -i

    def _prefix_sum(self, i: int) -> int:
        """Computes the prefix sum from [i, i], O(log(n))."""
        prefix_sum = 0
        while i != 0:
            prefix_sum += self._tree[i]
            i &= ~self._lsb(i)  # i -= self._lsb(i)

        return prefix_sum

    def sum(self, left: int, right: int) -> int:
        """Computes the sum of the interval [left, right], O(log(n))."""
        if right < left: raise ValueError('Make sure right >= left.')
        return self._prefix_sum(right) - self._prefix_sum(left - 1)

    def get(self, i: int) -> int:
        """Returns the value at index i."""
        return self.sum(i, i)

    def add(self, i: int, v: int) -> int:
        """Adds v to index i."""
        while i < self._n:
            self._tree[i] += v
            i += self._lsb(i)

    def set(self, i: int, v: int) -> int:
        """Sets index i to be equal to v."""
        return self.add(i, v - self.sum(i, i))

    def __str__(self) -> str:
        return str(self._tree)
