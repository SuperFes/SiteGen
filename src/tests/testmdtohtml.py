import unittest
from src.mdtohtml import split_nodes_by_delimiter, extract_md_images, extract_md_links, text_to_text_nodes, \
    markdown_to_blocks
from src.textnode import TextNode, TextType


class TestMDToHTML(unittest.TestCase):
    def test_bold_splitter(self):
        node = TextNode("This is a **bold text** node", TextType.Normal)
        nodes = split_nodes_by_delimiter([node],'**',TextType.Bold)
        self.assertEqual(str(nodes), "[TextNode(This is a, , None), TextNode(bold text, strong, None), TextNode(node, , None)]")

    def test_italic_splitter(self):
        node = TextNode("This is an *italic text* node", TextType.Normal)
        nodes = split_nodes_by_delimiter([node],'*',TextType.Italic)
        self.assertEqual(str(nodes), "[TextNode(This is an, , None), TextNode(italic text, em, None), TextNode(node, , None)]")

    def test_code_splitter(self):
        node = TextNode("This is a `code text` node", TextType.Normal)
        nodes = split_nodes_by_delimiter([node],'`',TextType.Code)
        self.assertEqual(str(nodes), "[TextNode(This is a, , None), TextNode(code text, code, None), TextNode(node, , None)]")

    def test_link_extractor(self):
        node = TextNode("This is a [link](https://example.org/) node", TextType.Normal)
        nodes = extract_md_links([node])
        self.assertEqual(str(nodes), "[TextNode(This is a , , None), TextNode(link, a, https://example.org/), TextNode( node, , None)]")

    def test_image_extractor(self):
        node = TextNode("This is an ![image](https://example.org/) node", TextType.Normal)
        nodes = extract_md_images([node])
        self.assertEqual(str(nodes), "[TextNode(This is an , , None), TextNode(image, img, https://example.org/), TextNode( node, , None)]")

    def test_text_to_nodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_text_nodes(text)
        self.assertEqual(str(nodes), "[TextNode(This is, , None), TextNode(text, , None), TextNode(with an, , None), TextNode(italic, , None), TextNode(word and a, , None), TextNode(code block, , None), TextNode(and an , , None), TextNode(obi wan image, , None), TextNode( and a , , None), TextNode(link, a, https://boot.dev)]")

    def test_md_to_blocks(self):
        text = "This is a text block\n\nThis is another text block"
        blocks = markdown_to_blocks(text)
        self.assertEqual(str(blocks), "['This is a text block', 'This is another text block']")
