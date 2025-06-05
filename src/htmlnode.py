
class HTMLNode:
    def __init__(self,tag=None, value=None, children=None, props=None):
        self.tag = tag 
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}

    def to_html(self):
        raise NotImplementedError("Subclasses must implement to_html")

    def props_to_html(self):
        if not self.props:
           return ""
        return " " + " ".join(f'{key}="{value}"' for key, value in self.props.items())
   
    def __repr__(self):
        return (
            f"HTMLNode(tag={self.tag!r}, value={self.value!r}, "
            f"children={self.children!r}, props={self.props!r})"
        )
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if value is None:
            raise ValueError("LeafNode requires a non-None value for value")
        super().__init__(tag=tag, value=value, children=[], props=props)

    def to_html(self):
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if tag is None:
            raise ValueError("ParentNode requires a non-None tag")
        if children is None:
            raise ValueError("ParentNode requires a non-None children list")
        if not isinstance(children, list):
            raise TypeError("children must be a list of HTMLNode instances")
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode cannot render without a tag")

        if self.children is None:
            raise ValueError("ParentNode cannot render without children")

        inner_html = "".join(child.to_html() for child in self.children)
        return f"<{self.tag}{self.props_to_html()}>{inner_html}</{self.tag}>"


        

    
