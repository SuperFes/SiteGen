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

    search_len = len(delimiter) + 1

    for node in nodes:
        if not delimiter in node.text:
            new_nodes.append(node)
            continue

        text = node.text

        while (True):
            delim_start = text.find(f" {delimiter}")
            delim_end = text.find(f"{delimiter} ")

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

    :param text: text to extract images from
    :return: list of text nodes
    """
    new_nodes = []

    for node in nodes:
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

    :param text: text to extract links from
    :return: list of text nodes
    """
    new_nodes = []

    for node in nodes:
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