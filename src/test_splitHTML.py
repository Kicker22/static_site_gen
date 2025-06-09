
from textnode import TextType, TextNode
from splitHTML import split_nodes_delimiter
from split_nodes_image import split_nodes_image
from split_nodes_link import split_nodes_link


def test_split_code_delimiter():
    input_nodes = [TextNode("This is `code`", TextType.TEXT)]
    output = split_nodes_delimiter(input_nodes, "`", TextType.CODE)
    assert output == [
        TextNode("This is ", TextType.TEXT),
        TextNode("code", TextType.CODE),
    ]

def test_split_multiple_bold():
    input_nodes = [TextNode("**bold** and **strong**", TextType.TEXT)]
    output = split_nodes_delimiter(input_nodes, "**", TextType.BOLD)
    assert output == [
        TextNode(" and ", TextType.TEXT),
        TextNode("bold", TextType.BOLD),
        TextNode(" and ", TextType.TEXT),
        TextNode("strong", TextType.BOLD),
    ]

def test_ignore_non_text_nodes():
    input_nodes = [TextNode("Bold", TextType.BOLD)]
    output = split_nodes_delimiter(input_nodes, "**", TextType.BOLD)
    assert output == [TextNode("Bold", TextType.BOLD)]

def test_raises_on_unmatched_delimiter():
    input_nodes = [TextNode("this is `broken", TextType.TEXT)]
    try:
        split_nodes_delimiter(input_nodes, "`", TextType.CODE)
        assert False  # should not reach here
    except ValueError as e:
        assert "Unmatched delimiter" in str(e)


def test_split_images(self):
    node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_image([node])
    self.assertListEqual(
        [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
        ],
        new_nodes,
    )

def test_split_links(self):
    node = TextNode(
        "Here's [Boot.dev](https://www.boot.dev) and [YouTube](https://youtube.com)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_link([node])
    self.assertListEqual(
        [
            TextNode("Here's ", TextType.TEXT),
            TextNode("Boot.dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("YouTube", TextType.LINK, "https://youtube.com"),
        ],
        new_nodes,
    )

