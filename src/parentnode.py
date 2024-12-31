from src.htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, attributes=None):
        super().__init__(tag, None, attributes, children)

    def __repr__(self):
        return f"ParentNode({self.tag}, {self.attributes}, {self.children})"
