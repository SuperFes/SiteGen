from enum import StrEnum


class Block:
    class Type(StrEnum):
        Paragraph = "p",
        Heading1 = "h1",
        Heading2 = "h2",
        Heading3 = "h3",
        Heading4 = "h4",
        Heading5 = "h5",
        Heading6 = "h6",
        Blockquote = "blockquote",
        CodeBlock = "code",
        UnorderedList = "ul",
        OrderedList = "ol",
        ListItem = "li",

    def __init__(self, block_type, children=None):
        self.block_type = block_type
        self.children = children or []
