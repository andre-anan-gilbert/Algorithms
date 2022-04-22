"""An implementation of a fenwick tree."""
import copy


class FenwickTree:
    """Class that represents a fenwick tree.

    Attributes:
        _n: The size of the array holding the tree values.
        _tree: The array containing the range values.
    """

    def __init__(self) -> None:
        self._n = 0
        self._tree = None

    def create_tree(self, values: list[int]) -> None:
        """Constructs the fenwick tree with initial values."""
        if values is None: raise ValueError('Values array cannot be None.')

        self._n = len(values)
        values[0] = 0

        self._tree = copy.deepcopy(values)

        for i in range(self._n):
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

    def interval_sum(self, left: int, right: int) -> int:
        """Computes the sum of the interval [left, right], O(log(n))."""
        if right < left: raise ValueError('Make sure right >= left.')
        return self._prefix_sum(right) - self._prefix_sum(left - 1)

    def get(self, i: int) -> int:
        """Returns the value at index i."""
        return self.interval_sum(i, i)

    def add(self, i: int, v: int) -> int:
        """Adds v to index i."""
        while i < self._n:
            self._tree[i] += v
            i += self._isb(i)

    def set(self, i: int, v: int) -> int:
        """Sets index i to be equal to v."""
        return self.add(i, v - self.interval_sum(i, i))

    def __str__(self) -> str:
        return str(self._tree)
