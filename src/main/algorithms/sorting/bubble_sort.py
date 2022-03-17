"""An implementation of bubble sort.

Time Complexity: O(n²).
"""


class BubbleSort:
    """Class that sorts arrays using bubble sort."""

    def sort_array(self, values: list[int]) -> None:
        self._bubble_sort(values)

    def _bubble_sort(self, array: list[int]) -> None:
        """Sorts the array using bubble sort."""
        if not array: return

        is_sorted = False
        while not is_sorted:
            is_sorted = True
            for i in range(1, len(array)):
                if array[i] < array[i - 1]:
                    self._swap(array, i - 1, i)
                    is_sorted = False

    def _swap(self, arr: list[int], i: int, j: int) -> None:
        arr[i], arr[j] = arr[j], arr[i]

    def main(self) -> None:
        array = [10, 4, 6, 8, 13, 2, 3]
        self.sort_array(array)
        print(array)


if __name__ == '__main__':
    BubbleSort().main()
