import unittest

from src.blocktype import Block
from src.mdtohtml import split_nodes_by_delimiter, extract_md_images, extract_md_links, text_to_text_nodes, \
    markdown_to_blocks, get_block_type, markdown_to_html_node, extract_title
from src.textnode import TextNode, TextType


class TestMDToHTML(unittest.TestCase):
    def test_bold_splitter(self):
        node = TextNode("This is a **bold text** node", TextType.Normal)
        nodes = split_nodes_by_delimiter([node],'**',TextType.Bold)
        self.assertEqual(str(nodes), "[TextNode(This is a , , None), TextNode(bold text, strong, None), TextNode( node, , None)]")

    def test_italic_splitter(self):
        node = TextNode("This is an *italic text* node", TextType.Normal)
        nodes = split_nodes_by_delimiter([node],'*',TextType.Italic)
        self.assertEqual(str(nodes), "[TextNode(This is an , , None), TextNode(italic text, em, None), TextNode( node, , None)]")

    def test_code_splitter(self):
        node = TextNode("This is a `code text` node", TextType.Normal)
        nodes = split_nodes_by_delimiter([node],'`',TextType.Code)
        self.assertEqual(str(nodes), "[TextNode(This is a , , None), TextNode(code text, code, None), TextNode( node, , None)]")

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
        self.assertEqual(str(nodes), "[TextNode(This is , , None), TextNode(text, strong, None), TextNode( with an , , None), TextNode(italic, em, None), TextNode( word and a , , None), TextNode(code block, code, None), TextNode( and an , , None), TextNode(obi wan image, img, https://i.imgur.com/fJRm4Vk.jpeg), TextNode( and a , , None), TextNode(link, a, https://boot.dev)]")

    def test_md_to_blocks(self):
        text = "This is a text block\n\nThis is another text block"
        blocks = markdown_to_blocks(text)
        self.assertEqual(str(blocks), "['This is a text block', 'This is another text block']")

    def test_block_types(self):
        text = "# This is a heading1 block\n\n```\nThis is a code block\n```\n\n* This is a list block\n* Item 2\n\n1. This is a numbered list block\n2. Item 2\n\nThis is a text block"
        blocks = markdown_to_blocks(text)

        for block in blocks:
            if block.startswith("#"):
                self.assertEqual(get_block_type(block), Block.Type.Heading1)
            elif block.startswith("```"):
                self.assertEqual(get_block_type(block), Block.Type.CodeBlock)
            elif block.startswith("*"):
                self.assertEqual(get_block_type(block), Block.Type.UnorderedList)
            elif block.startswith("1."):
                self.assertEqual(get_block_type(block), Block.Type.OrderedList)
            else:
                self.assertEqual(get_block_type(block), Block.Type.Paragraph)

    def test_md_to_html(self):
        text = "# This is a heading1 block\n\n```\nThis is a code block\n```\n\n* This is a list block\n* Item 2\n\n1. This is a numbered list block\n2. Item 2\n\nThis is a text block\n\nThis is text, **bold**, *italic*, `a code block`, an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg), and a [link](https://boot.dev)"

        html = markdown_to_html_node(text)

        self.assertEqual(str(html), "<div><h1>This is a heading1 block</h1><code>\nThis is a code block\n</code><ul><li>This is a list block</li><li>Item 2</li></ul><ol><li>This is a numbered list block</li><li>Item 2</li></ol><p>This is a text block</p><p>This is text, <strong>bold</strong>, <em>italic</em>, <code>a code block</code>, an <img src=\"https://i.imgur.com/fJRm4Vk.jpeg\" alt=\"obi wan image\">None</img>, and a <a href=\"https://boot.dev\">link</a></p></div>")

    def test_extract_title(self):
        text = "# This is a heading1 block\n\n```\nThis is a code block\n```\n\n* This is a list block\n* Item 2"

        title = extract_title(text)

        self.assertEqual(title, "This is a heading1 block")
