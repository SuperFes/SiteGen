import unittest

from src.htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "This is a paragraph")
        node2 = HTMLNode("p", "This is a paragraph")
        self.assertEqual(node, node2)

    def test_repr(self):
        node_text = HTMLNode("p", "This is a paragraph", {"class": "paragraph"}).__repr__()
        self.assertEqual(node_text, "HTMLNode(p, This is a paragraph, {'class': 'paragraph'}, [])")

    def test_str(self):
        node = HTMLNode("p", "This is a paragraph")
        self.assertEqual(str(node), "<p>This is a paragraph</p>")
