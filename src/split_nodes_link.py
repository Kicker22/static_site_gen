from transform import extract_markdown_links
from textnode import TextNode, TextType


def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        links = extract_markdown_links(text)

        if not links:
            new_nodes.append(node)
            continue

        idx = 0
        for label, url in links:
            full_syntax = f"[{label}]({url})"
            split_start = text.find(full_syntax, idx)

            if split_start > idx:
                new_nodes.append(TextNode(text[idx:split_start], TextType.TEXT))

            new_nodes.append(TextNode(label, TextType.LINK, url))
            idx = split_start + len(full_syntax)

        if idx < len(text):
            new_nodes.append(TextNode(text[idx:], TextType.TEXT))

    return new_nodes
