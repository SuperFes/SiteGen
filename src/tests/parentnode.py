import unittest

from src.parentnode import ParentNode

class TestParentNode(unittest.TestCase):
    def test_eq(self):
        node = ParentNode("a", [], {"href": "https://example.org/"})
        node2 = ParentNode("a", [], {"href": "https://example.org/"})
        self.assertEqual(node, node2)

    def test_repr(self):
        node_text = ParentNode("a", [], {"href": "https://example.org/"}).__repr__()
        self.assertEqual(node_text, "ParentNode(a, {'href': 'https://example.org/'}, [])")

    def test_children(self):
        node = ParentNode("a", [], {"href": "https://example.org/"})
        node.add_child(ParentNode("b", [], {"href": "https://example.org/"}))
        self.assertEqual(node.children, [ParentNode("b", [], {"href": "https://example.org/"})])
