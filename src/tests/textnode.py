import unittest

from src.textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.Bold)
        node2 = TextNode("This is a text node", TextType.Bold)
        self.assertEqual(node, node2)

    def test_repr(self):
        node_text = TextNode("This is a text node", TextType.Bold, "https://example.org/").__repr__()
        self.assertEqual(node_text, "TextNode(This is a text node, strong, https://example.org/)")

    def test_to_html_node(self):
        node = TextNode("This is a text node", TextType.Bold)
        html_node = node.to_html_node()
        self.assertEqual(html_node.tag, "strong")
        self.assertEqual(html_node.value, "This is a text node")

        node = TextNode("This is a text node", TextType.Image, "https://example.org/")
        html_node = node.to_html_node()
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, None)
        self.assertEqual(html_node.attributes, {"src": "https://example.org/"})

        node = TextNode("This is a text node", TextType.Normal)
        html_node = node.to_html_node()
        self.assertEqual(html_node.tag, "p")
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node.attributes, {})


if __name__ == "__main__":
    unittest.main()
