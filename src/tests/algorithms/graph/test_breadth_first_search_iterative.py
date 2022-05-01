"""Tests the iterative breadth first search implementation."""
import unittest
from main.algorithms.graph.breadth_first_search_iterative import BreadthFirstSearchIterative


class TestBreadthFirstSearchIterative(unittest.TestCase):
    """Class that tests the breadth first search implementation."""

    def test_none_graph_input(self) -> None:
        with self.assertRaises(ValueError):
            BreadthFirstSearchIterative(None)

    def test_singelton_graph(self) -> None:
        n = 1
        graph = BreadthFirstSearchIterative.create_empty_graph(n)
        solver = BreadthFirstSearchIterative(graph)

        path = solver.reconstruct_path(0, 0)
        expected = [0]
        self.assertEqual(path, expected)

    def test_two_node_graph(self) -> None:
        n = 2
        graph = BreadthFirstSearchIterative.create_empty_graph(n)
        BreadthFirstSearchIterative.add_unweighted_undirected_edge(graph, 0, 1)
        solver = BreadthFirstSearchIterative(graph)

        path = solver.reconstruct_path(0, 1)
        expected = [0, 1]
        self.assertEqual(path, expected)

    def test_three_node_graph(self) -> None:
        n = 3
        graph = BreadthFirstSearchIterative.create_empty_graph(n)
        BreadthFirstSearchIterative.add_unweighted_undirected_edge(graph, 0, 1)
        BreadthFirstSearchIterative.add_unweighted_undirected_edge(graph, 2, 1)
        solver = BreadthFirstSearchIterative(graph)

        path = solver.reconstruct_path(0, 2)
        expected = [0, 1, 2]
        self.assertEqual(path, expected)
