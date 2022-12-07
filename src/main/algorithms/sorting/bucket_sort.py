"""An implementation of bucket sort - O(n + k)."""


class BucketSort:
    """Class that sorts arrays using bucket sort."""

    def sort(self, array: list[int]) -> None:
        if not array: return

        min_value = min(array)
        max_value = max(array)
        if min_value == max_value: return
        self._bucket_sort(array, min_value, max_value)

    def _bucket_sort(self, array: list[int], min_value: int, max_value: int) -> None:
        size = len(array)
        m = max_value - min_value + 1
        number_of_buckets = m // size + 1
        buckets = [[] for _ in range(number_of_buckets)]
        for i in range(size):
            bucket_index = (array[i] - min_value) // m
            buckets[bucket_index].append(array[i])

        j = 0
        for bucket_index in range(number_of_buckets):
            bucket = buckets[bucket_index]
            if bucket is not None:
                bucket.sort()
                for k in range(len(bucket)):
                    array[j] = bucket[k]
                    j += 1


def main() -> None:
    sorter = BucketSort()
    array = [10, 4, 6, 4, 8, -13, 2, 3]
    sorter.sort(array)
    print(array)


if __name__ == '__main__':
    main()
