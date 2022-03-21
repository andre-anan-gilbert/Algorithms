"""An implementation of binary search - O(log(n))."""


class BinarySearch:
    """Class that searches an element using binary search."""
    _EPS = 0.00000001

    def binary_search(self, array: list[int], target: int) -> int:
        """Returns the index of the target element in the array, otherwise returns -1."""
        if not array: return

        low = 0
        high = len(array) - 1

        while low <= high:
            mid = (low + high) // 2
            if array[mid] == target:
                return mid
            elif array[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return -1

    def binary_search_sqrt(self, low: float, high: float, target: float) -> float:
        """Returns the square root of the target element."""
        if high <= low: raise ValueError('High should be higher than low.')

        while (high - low) > self._EPS:
            mid = (low + high) / 2.0

            value = mid * mid

            if value < target:
                low = mid
            else:
                high = mid

        return mid


def main() -> None:
    binary_search = BinarySearch()
    array = [-13, 2, 3, 4, 4, 6, 8, 10]
    print(binary_search.binary_search(array, 2))
    print(binary_search.binary_search(array, 40))

    low = 0.0
    high = 375.0
    target = 375.0
    print(binary_search.binary_search_sqrt(low, high, target))


if __name__ == '__main__':
    main()
