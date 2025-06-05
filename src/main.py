from textnode import TextNode
# main entry func
def main():
    node = TextNode('This is a test', "Link", "https://example.com")
    return print(repr(node))

main()