"""Tests the binary heap implementation of a priority queue."""
import random
import unittest
from heapq import heapify
from queue import PriorityQueue
from main.data_structures.priority_queue.binary_heap import BinaryHeap


class TestBinaryHeap(unittest.TestCase):
    """Class that tests the heap priority queue."""

    def setUp(self) -> None:
        self._loops = 100
        self._max_sz = 100
        self._priority_queue = BinaryHeap()

    def test_empty(self) -> None:
        self.assertEqual(self._priority_queue.size(), 0)
        self.assertTrue(self._priority_queue.is_empty())
        self.assertEqual(self._priority_queue.poll(), None)
        self.assertEqual(self._priority_queue.peek(), None)

    def test_heap_property(self) -> None:
        nums = [3, 2, 5, 6, 7, 9, 4, 8, 1]

        for num in nums:
            self._priority_queue.add(num)
        for i in range(1, 10):
            self.assertEqual(self._priority_queue.poll(), i)

        self._priority_queue.clear()

        self._priority_queue.heapify(nums)
        for i in range(1, 10):
            self.assertEqual(self._priority_queue.poll(), i)

    def test_heapify(self) -> None:
        for i in range(self._loops):
            nums = self._generate_random_list(i)

            self._priority_queue.heapify(nums)
            pq = PriorityQueue()
            for num in nums:
                pq.put(num)

            while not pq.empty():
                self.assertEqual(self._priority_queue.poll(), pq.get())

    def test_clear(self) -> None:
        strs = ['aa', 'bb', 'cc', 'dd', 'ee']

        self._priority_queue.heapify(strs)
        self._priority_queue.clear()
        self.assertEqual(self._priority_queue.size(), 0)
        self.assertTrue(self._priority_queue.is_empty())

    def test_contains(self) -> None:
        strs = ['aa', 'bb', 'cc', 'dd', 'ee']

        self._priority_queue.heapify(strs)
        self._priority_queue.remove('aa')
        self.assertFalse(self._priority_queue.contains('aa'))
        self._priority_queue.remove('bb')
        self.assertFalse(self._priority_queue.contains('bb'))
        self._priority_queue.remove('cc')
        self.assertFalse(self._priority_queue.contains('cc'))
        self._priority_queue.remove('dd')
        self.assertFalse(self._priority_queue.contains('dd'))
        self._priority_queue.clear()
        self.assertFalse(self._priority_queue.contains('ee'))

    def test_contains_randomized(self) -> None:
        for _ in range(self._loops):
            nums = self._generate_random_list(100)

            pq = PriorityQueue()
            for i in range(len(nums)):
                self._priority_queue.add(nums[i])
                pq.put(nums[i])

            for j in range(len(nums)):
                rand_num = nums[j]
                pq_contains_rand_num = False
                for k in range(pq.qsize()):
                    if pq.queue[k] == rand_num:
                        pq_contains_rand_num = True
                        remove_index = k

                self.assertEqual(self._priority_queue.contains(rand_num), pq_contains_rand_num)

                self._priority_queue.remove(rand_num)
                del pq.queue[remove_index]
                heapify(pq.queue)
                if rand_num not in pq.queue:
                    pq_contains_rand_num = False

                self.assertEqual(self._priority_queue.contains(rand_num), pq_contains_rand_num)

    def sequential_removing(self, arr: list[int], remove_order: list[int]) -> None:
        self.assertEqual(len(arr), len(remove_order))

        self._priority_queue.heapify(arr)
        pq = PriorityQueue()
        for val in arr:
            pq.put(val)

        for i in range(len(remove_order)):
            elem = remove_order[i]

            self.assertEqual(self._priority_queue.peek(), pq.queue[0])
            for j in range(pq.qsize()):
                if pq.queue[j] == elem:
                    del pq.queue[j]
                    break

            heapify(pq.queue)
            self._priority_queue.remove(elem)

            self.assertEqual(self._priority_queue.size(), pq.qsize())

        self.assertTrue(self._priority_queue.is_empty())

    def test_removing(self) -> None:
        arr = [1, 2, 3, 4, 5, 6, 7]
        remove_order = [1, 3, 6, 4, 5, 7, 2]
        self.sequential_removing(arr, remove_order)

        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        remove_order = [7, 4, 6, 10, 2, 5, 11, 3, 1, 8, 9]
        self.sequential_removing(arr, remove_order)

        arr = [8, 1, 3, 3, 5, 3]
        remove_order = [3, 3, 5, 8, 1, 3]
        self.sequential_removing(arr, remove_order)

        arr = [7, 7, 3, 1, 1, 2]
        remove_order = [2, 7, 1, 3, 7, 1]
        self.sequential_removing(arr, remove_order)

        arr = [32, 66, 93, 42, 41, 91, 54, 64, 9, 35]
        remove_order = [32, 66, 93, 42, 41, 91, 54, 64, 9, 35]
        self.sequential_removing(arr, remove_order)

    def test_removing_duplicates(self) -> None:
        arr = [2, 7, 2, 11, 7, 13, 2]

        self._priority_queue.heapify(arr)
        self.assertEqual(self._priority_queue.peek(), 2)
        self._priority_queue.add(3)

        self.assertEqual(self._priority_queue.poll(), 2)
        self.assertEqual(self._priority_queue.poll(), 2)
        self.assertEqual(self._priority_queue.poll(), 2)
        self.assertEqual(self._priority_queue.poll(), 3)
        self.assertEqual(self._priority_queue.poll(), 7)
        self.assertEqual(self._priority_queue.poll(), 7)
        self.assertEqual(self._priority_queue.poll(), 11)
        self.assertEqual(self._priority_queue.poll(), 13)

    def test_randomized_polling(self) -> None:
        for i in range(self._loops):
            nums = self._generate_random_list(i)
            pq = PriorityQueue()

            for num in nums:
                self._priority_queue.add(num)
                pq.put(num)

            while not pq.empty():
                self.assertEqual(self._priority_queue.size(), pq.qsize())
                self.assertEqual(self._priority_queue.peek(), pq.queue[0])

                pq_contains_peek_val = False
                for j in range(pq.qsize()):
                    if pq.queue[j] == self._priority_queue.peek():
                        pq_contains_peek_val = True

                self.assertEqual(self._priority_queue.contains(self._priority_queue.peek()), pq_contains_peek_val)

                v1 = self._priority_queue.poll()
                v2 = pq.get()

                self.assertEqual(v1, v2)
                self.assertEqual(self._priority_queue.peek(), pq.queue[0] if pq.qsize() > 0 else None)
                self.assertEqual(self._priority_queue.size(), pq.qsize())

    def test_randomized_removing(self) -> None:
        for i in range(self._loops):
            nums = self._generate_random_list(i)
            pq = PriorityQueue()

            for num in nums:
                self._priority_queue.add(num)
                pq.put(num)

            random.shuffle(nums)
            index = 0

            while not pq.empty():
                remove_num = nums[index]

                self.assertEqual(self._priority_queue.size(), pq.qsize())
                self.assertEqual(self._priority_queue.peek(), pq.queue[0])

                self._priority_queue.remove(remove_num)
                for j in range(pq.qsize()):
                    if pq.queue[j] == remove_num:
                        del pq.queue[j]
                        break

                heapify(pq.queue)

                self.assertEqual(self._priority_queue.peek(), pq.queue[0] if pq.qsize() > 0 else None)
                self.assertEqual(self._priority_queue.size(), pq.qsize())

                index += 1

    def test_reusebility(self) -> None:
        sizes = self._generate_unique_random_list(self._loops)
        pq = PriorityQueue()

        for size in sizes:
            self._priority_queue.clear()
            pq.queue.clear()

            nums = self._generate_random_list(size)
            for num in nums:
                self._priority_queue.add(num)
                pq.put(num)

            random.shuffle(nums)

            for i in range(size // 2):
                if 0.25 < random.uniform(0.0, 1.0):
                    rand_num = int(random.uniform(0.0, 1.0) * 10000)
                    self._priority_queue.add(rand_num)
                    pq.put(rand_num)

                remove_num = nums[i]

                self.assertEqual(self._priority_queue.size(), pq.qsize())
                self.assertEqual(self._priority_queue.peek(), pq.queue[0])

                self._priority_queue.remove(remove_num)
                for j in range(pq.qsize()):
                    if pq.queue[j] == remove_num:
                        del pq.queue[j]
                        break

                heapify(pq.queue)

                self.assertEqual(self._priority_queue.peek(), pq.queue[0])
                self.assertEqual(self._priority_queue.size(), pq.qsize())

    def _generate_random_list(self, size: int) -> list[int]:
        return [int(random.uniform(0.0, 1.0) * self._max_sz) for _ in range(0, size)]

    def _generate_unique_random_list(self, size: int) -> list[int]:
        array = list(range(size))
        random.shuffle(array)
        return array
