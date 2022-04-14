"""An implementation of a union find/disjoint set."""


class UnionFind:
    """Class that represents a union find/disjoint set.

    Attributes:
        _size: The number of elements in the union find.
        _num_components: The number of components in the union find.
        _sz: Tracks of the size of the components.
        _id: Tracks the components and its root node.
    """

    def __init__(self, size: int) -> None:
        if size <= 0: raise ValueError('Size must be > 0.')

        self._size = self._num_components = size
        self._sz = [1 for _ in range(size)]
        self._id = list(range(size))

    def find(self, p: int) -> int:
        """Finds the component p belongs to."""
        root = p
        while root != self._id[root]:
            root = self._id[root]

        while p != root:
            next_node = self._id[p]
            self._id[p] = root
            p = next_node

        return root

    def size(self) -> int:
        """Returns the size of the union find."""
        return self._size

    def components(self) -> int:
        """Returns the number of components in the union find."""
        return self._num_components

    def component_size(self, p: int) -> int:
        """Returns the size of component p."""
        return self._sz[self.find(p)]

    def connected(self, p: int, q: int) -> bool:
        """Checks if p & q belong to the same component."""
        return self.find(p) == self.find(q)

    def unify(self, p: int, q: int) -> None:
        """Merges the components containing p & q."""
        if self.connected(p, q): return

        root1 = self.find(p)
        root2 = self.find(q)

        if self._id[root1] < self._id[root2]:
            self._sz[root2] += self._sz[root1]
            self._id[root1] = self._id[root2]
            self._sz[root1] = 0
        else:
            self._sz[root1] += self._sz[root2]
            self._id[root2] = self._id[root1]
            self._sz[root2] = 0

        self._num_components -= 1


def main() -> None:
    union_find = UnionFind(10)
    print(union_find.size())
    print(union_find.components())
    union_find.unify(0, 1)
    union_find.unify(1, 2)
    union_find.unify(3, 4)
    union_find.unify(5, 6)
    union_find.unify(6, 7)
    print(union_find.size())
    print(union_find.components())
    print(union_find.find(0))
    print(union_find.component_size(0))
    print(union_find.connected(0, 2))


if __name__ == '__main__':
    main()
