"""Tests the singly linked list implementation."""
import random
import unittest
from collections import deque
from main.data_structures.linked_list.doubly_linked_list import DoublyLinkedList


class TestDoublyLinkedList(unittest.TestCase):
    """Class that tests the doubly linked list implementation."""

    def setUp(self) -> None:
        self._loops = 10000
        self._test_sz = 40
        self._num_nulls = self._test_sz // 5
        self._max_rand_num = 250
        self._linked_list = DoublyLinkedList()

    def test_empty_list(self) -> None:
        self.assertTrue(self._linked_list.is_empty())
        self.assertEqual(self._linked_list.size(), 0)

    def test_remove_first_of_empty(self) -> None:
        self.assertRaises(Exception, self._linked_list.remove_first)

    def test_remove_last_of_empty(self) -> None:
        self.assertRaises(Exception, self._linked_list.remove_last)

    def test_peek_first_of_empty(self) -> None:
        self.assertRaises(Exception, self._linked_list.peek_first)

    def test_PeekLastOfEmpty(self) -> None:
        self.assertRaises(Exception, self._linked_list.peek_last)

    def test_add_first(self) -> None:
        self._linked_list.add_first(3)
        self.assertEqual(self._linked_list.size(), 1)
        self._linked_list.add_first(5)
        self.assertEqual(self._linked_list.size(), 2)

    def test_add_last(self) -> None:
        self._linked_list.add_last(3)
        self.assertEqual(self._linked_list.size(), 1)
        self._linked_list.add_last(5)
        self.assertEqual(self._linked_list.size(), 2)

    def test_add_at(self) -> None:
        self._linked_list.add_at(0, 1)
        self.assertEqual(self._linked_list.size(), 1)
        self._linked_list.add_at(1, 2)
        self.assertEqual(self._linked_list.size(), 2)
        self._linked_list.add_at(1, 3)
        self.assertEqual(self._linked_list.size(), 3)
        self._linked_list.add_at(2, 4)
        self.assertEqual(self._linked_list.size(), 4)
        self._linked_list.add_at(1, 8)
        self.assertEqual(self._linked_list.size(), 5)

    def test_remove_first(self) -> None:
        self._linked_list.add_first(3)
        self.assertTrue(self._linked_list.remove_first() == 3)
        self.assertTrue(self._linked_list.is_empty())

    def test_remove_last(self) -> None:
        self._linked_list.add_last(4)
        self.assertTrue(self._linked_list.remove_last() == 4)
        self.assertTrue(self._linked_list.is_empty())

    def test_peek_first(self) -> None:
        self._linked_list.add_first(4)
        self.assertTrue(self._linked_list.peek_first() == 4)
        self.assertEqual(self._linked_list.size(), 1)

    def test_peek_last(self) -> None:
        self._linked_list.add_last(4)
        self.assertTrue(self._linked_list.peek_last() == 4)
        self.assertEqual(self._linked_list.size(), 1)

    def test_peeking(self) -> None:
        # 5
        self._linked_list.add_first(5)
        self.assertTrue(self._linked_list.peek_first() == 5)
        self.assertTrue(self._linked_list.peek_last() == 5)

        # 6 - 5
        self._linked_list.add_first(6)
        self.assertTrue(self._linked_list.peek_first() == 6)
        self.assertTrue(self._linked_list.peek_last() == 5)

        # 7 - 6 - 5
        self._linked_list.add_first(7)
        self.assertTrue(self._linked_list.peek_first() == 7)
        self.assertTrue(self._linked_list.peek_last() == 5)

        # 7 - 6 - 5 - 8
        self._linked_list.add_last(8)
        self.assertTrue(self._linked_list.peek_first() == 7)
        self.assertTrue(self._linked_list.peek_last() == 8)

        # 7 - 6 - 5
        self._linked_list.remove_last()
        self.assertTrue(self._linked_list.peek_first() == 7)
        self.assertTrue(self._linked_list.peek_last() == 5)

        # 7 - 6
        self._linked_list.remove_last()
        self.assertTrue(self._linked_list.peek_first() == 7)
        self.assertTrue(self._linked_list.peek_last() == 6)

        # 6
        self._linked_list.remove_first()
        self.assertTrue(self._linked_list.peek_first() == 6)
        self.assertTrue(self._linked_list.peek_last() == 6)

    def test_removing(self) -> None:
        self._linked_list.add('a')
        self._linked_list.add('b')
        self._linked_list.add('c')
        self._linked_list.add('d')
        self._linked_list.add('e')
        self._linked_list.add('f')
        self._linked_list.remove('b')
        self._linked_list.remove('a')
        self._linked_list.remove('d')
        self._linked_list.remove('e')
        self._linked_list.remove('c')
        self._linked_list.remove('f')
        self.assertEqual(0, self._linked_list.size())
        self._linked_list.clear()

    def test_remove_at(self) -> None:
        self._linked_list.add(1)
        self._linked_list.add(2)
        self._linked_list.add(3)
        self._linked_list.add(4)
        self._linked_list.remove_at(0)
        self._linked_list.remove_at(2)
        print(self._linked_list.peek_first())
        self.assertTrue(self._linked_list.peek_first() == 2)
        self.assertTrue(self._linked_list.peek_last() == 3)
        self._linked_list.remove_at(1)
        self._linked_list.remove_at(0)
        self.assertEqual(self._linked_list.size(), 0)

    def test_clear(self) -> None:
        self._linked_list.add(22)
        self._linked_list.add(33)
        self._linked_list.add(44)
        self.assertEqual(self._linked_list.size(), 3)
        self._linked_list.clear()
        self.assertEqual(self._linked_list.size(), 0)
        self._linked_list.add(22)
        self._linked_list.add(33)
        self._linked_list.add(44)
        self.assertEqual(self._linked_list.size(), 3)
        self._linked_list.clear()
        self.assertEqual(self._linked_list.size(), 0)

    def test_randomized_removing(self) -> None:
        linked_list = deque()
        for _ in range(0, self._loops):

            self._linked_list.clear()
            linked_list.clear()

            rand_nums = self._generate_random_list(self._test_sz)
            for num in rand_nums:
                linked_list.append(num)
                self._linked_list.add(num)

            random.shuffle(rand_nums)

            for i in range(0, len(rand_nums)):
                rm_val = rand_nums[i]
                self.assertEqual(linked_list.remove(rm_val), None)
                self.assertEqual(self._linked_list.remove(rm_val), True)
                self.assertEqual(len(linked_list), self._linked_list.size())

                iter1 = iter(linked_list)
                iter2 = iter(self._linked_list)

                while True:
                    dq_val = next(iter1, -1)
                    if dq_val == -1: break
                    ll_val = next(iter2, -1)
                    self.assertEqual(dq_val, ll_val)

    def test_randomized_remove_at(self) -> None:
        linked_list = deque()
        for _ in range(0, self._loops):

            self._linked_list.clear()
            linked_list.clear()

            rand_nums = self._generate_random_list(self._test_sz)
            for num in rand_nums:
                linked_list.append(num)
                self._linked_list.add(num)

            for _ in range(0, len(rand_nums)):
                rm_index = random.sample(range(0, self._linked_list.size()), 1)
                rm_index = rm_index[0]

                num1 = linked_list[rm_index]
                num2 = self._linked_list.remove_at(rm_index)
                del linked_list[rm_index]

                self.assertEqual(num1, num2)
                self.assertEqual(len(linked_list), self._linked_list.size())

                iter1 = iter(linked_list)
                iter2 = iter(self._linked_list)

                while True:
                    dq_val = next(iter1, -1)
                    if dq_val == -1: break
                    ll_val = next(iter2, -1)
                    self.assertEqual(dq_val, ll_val)

    def test_randomized_index_of(self) -> None:
        linked_list = deque()
        for _ in range(0, self._loops):

            self._linked_list.clear()
            linked_list.clear()

            rand_nums = self._generate_unique_random_list(self._test_sz)
            for num in rand_nums:
                linked_list.append(num)
                self._linked_list.add(num)

            random.shuffle(rand_nums)

            for i in range(0, len(rand_nums)):
                elem = rand_nums[i]
                index1 = linked_list.index(elem)
                index2 = self._linked_list.index_of(elem)

                self.assertEqual(index1, index2)
                self.assertEqual(len(linked_list), self._linked_list.size())

                iter1 = iter(linked_list)
                iter2 = iter(self._linked_list)

                while True:
                    dq_val = next(iter1, -1)
                    if dq_val == -1: break
                    ll_val = next(iter2, -1)
                    self.assertEqual(dq_val, ll_val)

    def test_to_string(self) -> None:
        self.assertEqual(str(self._linked_list), '[]')
        self._linked_list.add('a')
        self.assertEqual(str(self._linked_list), '[a]')
        self._linked_list.add('b')
        self.assertEqual(str(self._linked_list), '[a, b]')
        self._linked_list.add('c')
        self._linked_list.add('d')
        self._linked_list.add('e')
        self._linked_list.add('f')
        self.assertEqual(str(self._linked_list), '[a, b, c, d, e, f]')

    def _generate_random_list(self, size: int) -> list[int]:
        array = random.sample(range(0, self._max_rand_num), size)

        for _ in range(0, self._num_nulls):
            array.append(None)

        random.shuffle(array)
        return array

    def _generate_unique_random_list(self, size: int) -> list[int]:
        array = list(range(0, size))

        for _ in range(0, self._num_nulls):
            array.append(None)

        random.shuffle(array)
        return array
