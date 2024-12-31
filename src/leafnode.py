from src.htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag, value, attributes=None):
        super().__init__(tag, value, attributes)

    def __eq__(self, other):
        return (
                self.tag == other.tag and
                self.value == other.value and
                self.attributes == other.attributes
        )

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.attributes})"
    