from src.blocktype import Block
from src.htmlnode import HTMLNode
from src.textnode import TextNode, TextType


def split_nodes_by_delimiter(nodes, delimiter, text_type):
    """
    Split a list of nodes by a text delimiter and returns new text nodes based on the delimiter.

    :param nodes: list of nodes
    :param delimiter: delimiter used to split the nodes
    :param text_type: text type of the delimiter node
    :return: list of lists of nodes
    """
    new_nodes = []

    search_len = len(delimiter)

    for node in nodes:
        if not delimiter in node.text:
            new_nodes.append(node)
        else:
            text = node.text

            while (True):
                delim_start = text.find(f"{delimiter}")
                delim_end = text.find(f"{delimiter}", delim_start + search_len)

                if delim_start == -1 or delim_end == -1:
                    break

                left = node.text[0:delim_start]
                mid = node.text[delim_start + search_len:delim_end]
                text = node.text[delim_end + search_len:]

                if len(left):
                    new_nodes.append(TextNode(left, node.text_type))

                new_nodes.append(TextNode(mid, text_type))

            if len(text):
                new_nodes.append(TextNode(text, node.text_type))

    return new_nodes


def extract_md_images(nodes):
    """
    Extracts markdown images from a text and returns a list of text nodes.

    :param nodes:
    :return: list of text nodes
    """
    new_nodes = []

    for node in nodes:
        if not "![" in node.text:
            new_nodes.append(node)
        else:
            text = node.text

            while (True):
                img_start = text.find("![")
                img_end = text.find("]")

                if img_start == -1 or img_end == -1:
                    break

                left = text[0:img_start]
                alt_text = text[img_start + 2:img_end]

                url_start = text.find("(", img_end)
                url_end = text.find(")", url_start)

                if url_start == -1 or url_end == -1:
                    break

                url = text[url_start + 1:url_end]
                text = text[url_end + 1:]

                if len(left):
                    new_nodes.append(TextNode(left, TextType.Normal))

                new_nodes.append(TextNode(alt_text, TextType.Image, url))

            if len(text):
                new_nodes.append(TextNode(text, TextType.Normal))

    return new_nodes


def extract_md_links(nodes):
    """
    Extracts markdown links from a text and returns a list of text nodes.

    :param nodes:
    :return: list of text nodes
    """
    new_nodes = []

    for node in nodes:
        if not "[" in node.text:
            new_nodes.append(node)
        else:
            text = node.text

            while (True):
                link_start = text.find("[")
                link_end = text.find("]")

                if link_start == -1 or link_end == -1:
                    break

                left = text[0:link_start]
                mid = text[link_start + 1:link_end]

                url_start = text.find("(", link_end)
                url_end = text.find(")", url_start)

                if url_start == -1 or url_end == -1:
                    break

                url = text[url_start + 1:url_end]
                text = text[url_end + 1:]

                if len(left):
                    new_nodes.append(TextNode(left, TextType.Normal))

                new_nodes.append(TextNode(mid, TextType.Link, url))

            if len(text):
                new_nodes.append(TextNode(text, TextType.Normal))

    return new_nodes

def text_to_text_nodes(text):
    """
    Converts a text to a list of text nodes.

    :param text: text to convert
    :return: list of text nodes
    """
    nodes = [TextNode(text, TextType.Normal)]
    nodes = split_nodes_by_delimiter(nodes, "**", TextType.Bold)
    nodes = split_nodes_by_delimiter(nodes, "*", TextType.Italic)
    nodes = split_nodes_by_delimiter(nodes, "`", TextType.Code)
    nodes = extract_md_images(nodes)
    nodes = extract_md_links(nodes)

    return nodes

def markdown_to_blocks(markdown):
    """
    Converts markdown text to a list of text nodes.

    :param markdown: markdown text to convert
    :return: list of text blocks
    """
    blocks = markdown.split("\n\n")
    text_blocks = []

    for block in blocks:
        if len(block) == 0:
            continue

        text_blocks.append(block)

    return text_blocks

def get_block_type(block):
    """
    Converts a text block to a block type.

    :param block: text block
    :return: block type
    """
    if block.startswith("#" * 6):
        return Block.Type.Heading6
    if block.startswith("#" * 5):
        return Block.Type.Heading5
    if block.startswith("#" * 4):
        return Block.Type.Heading4
    if block.startswith("#" * 3):
        return Block.Type.Heading3
    if block.startswith("#" * 2):
        return Block.Type.Heading2
    if block.startswith("#"):
        return Block.Type.Heading1
    if block.startswith("-") or block.startswith("*"):
        return Block.Type.UnorderedList
    if block.startswith("1."):
        return Block.Type.OrderedList
    if block.startswith(">"):
        return Block.Type.Blockquote
    if block.startswith("```") and block.endswith("```"):
        return Block.Type.CodeBlock

    return Block.Type.Paragraph


def process_block(block):
    """
    Processes a text block and returns a text node.

    :param block: text block to process
    :return: text
    """
    block_type = get_block_type(block)

    if block_type == Block.Type.Heading1:
        return HTMLNode(block_type, block[2:])
    if block_type == Block.Type.Heading2:
        return HTMLNode(block_type, block[3:])
    if block_type == Block.Type.Heading3:
        return HTMLNode(block_type, block[4:])
    if block_type == Block.Type.Heading4:
        return HTMLNode(block_type, block[5:])
    if block_type == Block.Type.Heading5:
        return HTMLNode(block_type, block[6:])
    if block_type == Block.Type.Heading6:
        return HTMLNode(block_type, block[7:])
    if block_type == Block.Type.Blockquote:
        return HTMLNode(block_type, block.replace("> ", ""))
    if block_type == Block.Type.CodeBlock:
        return HTMLNode(block_type, block[3:-3])
    if block_type == Block.Type.UnorderedList:
        return HTMLNode(Block.Type.UnorderedList, None, None, list(map(lambda line: HTMLNode(Block.Type.ListItem, line[2:]), block.split("\n"))))
    if block_type == Block.Type.OrderedList:
        return HTMLNode(Block.Type.OrderedList, None, None, list(map(lambda line: HTMLNode(Block.Type.ListItem, line[3:]), block.split("\n"))))

    text_nodes = text_to_text_nodes(block)
    node = HTMLNode(block_type)
    node.text_to_children(text_nodes)

    return node


def markdown_to_html_node(markdown):
    """
    Converts markdown text to an html node.

    :param markdown: markdown text to convert
    :return: html node
    """
    # Create the parent
    html = HTMLNode("div")

    blocks = markdown_to_blocks(markdown)

    for block in blocks:
        node = process_block(block)
        html.add_child(node)

    return html
