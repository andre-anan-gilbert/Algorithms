"""An implementation of counting sort - O(n + k)."""


class CountingSort:
    """Class that sorts arrays using counting sort."""

    def sort(self, array: list[int]) -> None:
        if not array: return

        min_value = min(array)
        max_value = max(array)
        self._counting_sort(array, min_value, max_value)

    def _counting_sort(self, array: list[int], min_value: int, max_value: int) -> None:
        size = max_value - min_value + 1
        count = [0 for _ in range(size)]

        for i in range(len(array)):
            count[array[i] - min_value] += 1

        k = 0
        for i in range(size):
            while count[i] > 0:
                count[i] -= 1
                array[k] = i + min_value
                k += 1


def main() -> None:
    sorter = CountingSort()
    array = [10, 4, 6, 4, 8, -13, 2, 3]
    sorter.sort(array)
    print(array)


if __name__ == '__main__':
    main()
