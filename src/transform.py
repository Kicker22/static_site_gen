from htmlnode import LeafNode
from textnode import TextType, TextNode

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == TextType.ANCHOR:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == TextType.ALT:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    else:
        raise ValueError(f"Unsupported text type: {text_node.text_type}")
