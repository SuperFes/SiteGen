import unittest

from src.textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.Bold)
        node2 = TextNode("This is a text node", TextType.Bold)
        self.assertEqual(node, node2)

    def test_repr(self):
        node_text = TextNode("This is a text node", TextType.Bold, "https://example.org/").__repr__()
        self.assertEqual(node_text, "TextNode(This is a text node, ('strong',), https://example.org/)")


if __name__ == "__main__":
    unittest.main()
