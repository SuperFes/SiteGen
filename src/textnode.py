from enum import StrEnum

from src.leafnode import LeafNode


class TextType(StrEnum):
    Normal = "",
    Bold   = "strong",
    Italic = "em",
    Code   = "code",
    Link   = "a",
    Image  = "img"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
                self.text == other.text and
                self.text_type == other.text_type and
                self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

    def to_html_node(self):
        attributes = {}
        value = None

        if self.text_type == TextType.Link:
            value = self.text
            attributes = {"href": self.url}
        elif self.text_type == TextType.Image:
            attributes = {"src": self.url, "alt": self.text}
        else:
            value = self.text

        return LeafNode(self.text_type.value, value, attributes)
