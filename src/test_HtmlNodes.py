import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_with_multiple_attributes(self):
        node = HTMLNode(tag="a", value="Google", props={"href": "https://google.com", "target": "_blank"})
        self.assertIn('href="https://google.com"', node.props_to_html())
        self.assertIn('target="_blank"', node.props_to_html())

    def test_props_to_html_with_no_attributes(self):
        node = HTMLNode(tag="p", value="Hello world")
        self.assertEqual(node.props_to_html(), "")

    def test_repr_output(self):
        node = HTMLNode(tag="div", value="content", props={"id": "main"})
        expected_repr = "HTMLNode(tag='div', value='content', children=[], props={'id': 'main'})"
        self.assertEqual(repr(node), expected_repr)

    # test for leaf node below this line
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_with_single_prop(self):
        node = LeafNode("a", "Click me", {"href": "https://example.com"})
        self.assertEqual(node.to_html(), '<a href="https://example.com">Click me</a>')

    def test_leaf_to_html_with_multiple_props(self):
        node = LeafNode("img", "image", {"src": "image.jpg", "alt": "An image"})
        html = node.to_html()
        self.assertIn('<img', html)
        self.assertIn('src="image.jpg"', html)
        self.assertIn('alt="An image"', html)
        self.assertIn('>image</img>', html)
    
    def test_leafnode_raises_error_on_missing_value(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None)

    # these are test for parent nodes

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(),"<div><span><b>grandchild</b></span></div>",)

    def test_to_html_with_multiple_children(self):
        child1 = LeafNode("p", "Paragraph 1")
        child2 = LeafNode("p", "Paragraph 2")
        parent = ParentNode("section", [child1, child2])
        self.assertEqual(parent.to_html(), "<section><p>Paragraph 1</p><p>Paragraph 2</p></section>")

    def test_to_html_deep_nesting(self):
        leaf = LeafNode("em", "nested")
        inner = ParentNode("span", [leaf])
        middle = ParentNode("div", [inner])
        outer = ParentNode("section", [middle])
        expected = "<section><div><span><em>nested</em></span></div></section>"
        self.assertEqual(outer.to_html(), expected)
        
    def test_to_html_with_props(self):
        child = LeafNode("p", "content")
        parent = ParentNode("div", [child], {"id": "main", "class": "wrapper"})
        result = parent.to_html()
        self.assertIn('<div', result)
        self.assertIn('id="main"', result)
        self.assertIn('class="wrapper"', result)
        self.assertIn('<p>content</p>', result)


    def test_to_html_raises_on_none_children(self):
        with self.assertRaises(ValueError) as context:
            ParentNode("div", None).to_html()
        self.assertIn("children", str(context.exception))





if __name__ == "__main__":
    unittest.main()
