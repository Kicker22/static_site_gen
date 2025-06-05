
from textnode import TextType, TextNode
from splitHTML import split_nodes_delimiter


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
