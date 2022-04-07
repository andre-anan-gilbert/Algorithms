"""Tests the stack implementations."""
import unittest
from main.data_structures.stack.array_stack import ArrayStack
from main.data_structures.stack.linked_stack import LinkedStack


class TestStack(unittest.TestCase):
    """Class that tests the stack implementations."""

    def setUp(self) -> None:
        self._stacks = [ArrayStack(), LinkedStack()]

    def test_empty_stack(self) -> None:
        for stack in self._stacks:
            self.assertTrue(stack.is_empty())
            self.assertEqual(stack.size(), 0)

    def test_pop_on_empty(self) -> None:
        for stack in self._stacks:
            self.assertRaises(Exception, stack.pop)

    def test_peek_on_empty(self) -> None:
        for stack in self._stacks:
            self.assertRaises(Exception, stack.pop)

    def test_push(self) -> None:
        for stack in self._stacks:
            stack.push(2)
            self.assertEqual(stack.size(), 1)

    def test_peek(self) -> None:
        for stack in self._stacks:
            stack.push(2)
            self.assertEqual(2, int(stack.peek()))
            self.assertEqual(stack.size(), 1)

    def test_pop(self) -> None:
        for stack in self._stacks:
            stack.push(2)
            self.assertEqual(2, int(stack.pop()))
            self.assertEqual(stack.size(), 0)

    def test_exhaustively(self) -> None:
        for stack in self._stacks:
            self.assertTrue(stack.is_empty())
            stack.push(1)
            self.assertFalse(stack.is_empty())
            stack.push(2)
            self.assertEqual(stack.size(), 2)
            self.assertEqual(2, int(stack.peek()))
            self.assertEqual(stack.size(), 2)
            self.assertEqual(2, int(stack.pop()))
            self.assertEqual(stack.size(), 1)
            self.assertEqual(1, int(stack.peek()))
            self.assertEqual(stack.size(), 1)
            self.assertEqual(1, int(stack.pop()))
            self.assertEqual(stack.size(), 0)
            self.assertTrue(stack.is_empty())
