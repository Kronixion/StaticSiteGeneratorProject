class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        aggregator = ""
        for prop in props:
            aggregator += f"{prop}={props[prop]} "
        return aggregator

    def __repr__(self):
        return f"{self.tag}\n{self.value}\n{self.children}\n{self.props_to_html}"
