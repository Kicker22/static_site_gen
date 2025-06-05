import unittest
from htmlnode import HTMLNode

class testHTMLNode(unittest.TestCase):
    
    def test_not_empty(self):
        node = HTMLNode("Has", "a", 'value', "please")
        self.assertEqual(node.tag, "Has")
        self.assertEqual(node.value, "a")
        self.assertEqual(node.children, "value")
        self.assertEqual(node.props, "please")   
