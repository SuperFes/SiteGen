import unittest

from src.leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("a", "https://example.org/")
        node2 = LeafNode("a", "https://example.org/")
        self.assertEqual(node, node2)

    def test_repr(self):
        node_text = LeafNode("a", "https://example.org/").__repr__()
        self.assertEqual(node_text, "LeafNode(a, https://example.org/, {})")
