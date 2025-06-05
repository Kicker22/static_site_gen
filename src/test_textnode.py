import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):

    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)   
    
    def test_not_empty(self):
        node = TextNode("check", "code", 'https://example.com')
        self.assertEqual(node.text, 'check')
        self.assertEqual(node.text_type, 'code')
        self.assertEqual(node.url, "https://example.com")

    def test_url_is_none_by_default(self):
        node = TextNode("Hello", "italic")
        self.assertIsNone(node.url)
    
    def test_not_equal_when_url_differs(self):
        node1 = TextNode("hello", TextType.ANCHOR, "http://a.com")
        node2 = TextNode("hello", TextType.ANCHOR, "http://b.com")
        self.assertNotEqual(node1, node2)

    def test_not_equal_different_type(self):
        node = TextNode("hi", TextType.BOLD)
        self.assertNotEqual(node, "not a TextNode")


        
if __name__ == "__main__":
    unittest.main()