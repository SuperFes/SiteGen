class HTMLNode:
    def __init__(self, tag=None, value=None, attributes=None, children=None):
        self.tag = tag
        self.value = value
        self.attributes = attributes or {}
        self.children = children or []

    def attributes_to_html(self):
        if not self.attributes:
            return ''

        return ' ' + ' '.join(f'{key}="{value}"' for key, value in self.attributes.items())

    def add_attribute(self, key, value):
        self.attributes[key] = value

    def add_child(self, child):
        self.children.append(child)

    def __eq__(self, other):
        return (
                self.tag == other.tag and
                self.value == other.value and
                self.attributes == other.attributes and
                self.children == other.children
        )

    def __str__(self):
        # Just text
        if not self.tag:
            return self.value

        if not self.children:
            return f"<{self.tag}{self.attributes_to_html()}>{self.value}</{self.tag}>"

        return f"<{self.tag}{self.attributes_to_html()}>{''.join(str(child) for child in self.children)}</{self.tag}>"

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.attributes}, {self.children})"

    def text_to_children(self, text_nodes):
        for text_node in text_nodes:
            self.add_child(text_node.to_html_node())
        pass
