
class HTMLNode:
    def __init__(self,tag=None, value=None, children=None, props=None):
        self.tag = tag 
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError(self.children)

    def props_to_html(self):
        return f'{self.tag!r}, {self.props!r}'
    
    def __repr__(self):
        return f'HTMLNode({self.tag!r}, {self.value!r}, {self.children!r}, {self.props!r})'
    
