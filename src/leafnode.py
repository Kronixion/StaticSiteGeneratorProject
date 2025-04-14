from htmlnode import HTMLNode
class LeafNode(HTMLNode):
    def __init__(self, tag, value):
        super().__init__(tag, value, None, None)

    def to_html(self):
        if self.value == None:
            raise ValueError("This leaf node does not have a value.")
        if self.tag == None:
            return self.value
        return f"<{self.tag}>{self.value}</{self.tag}>"



