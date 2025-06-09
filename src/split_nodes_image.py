from textnode import TextNode, TextType
from transform import extract_markdown_images

def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        images = extract_markdown_images(text)

        if not images:
            new_nodes.append(node)
            continue

        # We'll track where we are in the string
        idx = 0
        for alt, url in images:
            full_syntax = f"![{alt}]({url})"
            split_start = text.find(full_syntax, idx)

            if split_start > idx:
                new_nodes.append(TextNode(text[idx:split_start], TextType.TEXT))

            new_nodes.append(TextNode(alt, TextType.IMAGE, url))
            idx = split_start + len(full_syntax)

        if idx < len(text):
            new_nodes.append(TextNode(text[idx:], TextType.TEXT))

    return new_nodes
