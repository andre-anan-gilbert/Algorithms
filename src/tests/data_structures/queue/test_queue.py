"""Tests the queue implementations."""
import unittest
from main.data_structures.queue.array_queue import ArrayQueue


class TestQueue(unittest.TestCase):
    """Class that tests the queue implementations."""

    def setUp(self) -> None:
        self._queues = [ArrayQueue()]

    def test_empty_queue(self) -> None:
        for queue in self._queues:
            self.assertTrue(queue.is_empty())
            self.assertEqual(queue.size(), 0)

    def test_poll_on_empty(self) -> None:
        for queue in self._queues:
            self.assertRaises(Exception, queue.poll)

    def test_peek_on_empty(self) -> None:
        for queue in self._queues:
            self.assertRaises(Exception, queue.peek)

    def test_offer(self) -> None:
        for queue in self._queues:
            queue.offer(2)
            self.assertEqual(queue.size(), 1)

    def test_peek(self) -> None:
        for queue in self._queues:
            queue.offer(2)
            self.assertEqual(2, int(queue.peek()))
            self.assertEqual(queue.size(), 1)

    def test_poll(self) -> None:
        for queue in self._queues:
            queue.offer(2)
            self.assertEqual(2, int(queue.poll()))
            self.assertEqual(queue.size(), 0)

    def test_exhaustively(self) -> None:
        for queue in self._queues:
            self.assertTrue(queue.is_empty())
            queue.offer(1)
            self.assertFalse(queue.is_empty())
            queue.offer(2)
            self.assertEqual(queue.size(), 2)
            self.assertEqual(1, int(queue.peek()))
            self.assertEqual(queue.size(), 2)
            self.assertEqual(1, int(queue.poll()))
            self.assertEqual(queue.size(), 1)
            self.assertEqual(2, int(queue.peek()))
            self.assertEqual(queue.size(), 1)
            self.assertEqual(2, int(queue.poll()))
            self.assertEqual(queue.size(), 0)
            self.assertTrue(queue.is_empty())
