import unittest

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_link,
    text_type_image
    )

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a test node", text_type_bold)
        node2 = TextNode("This is a test node", text_type_bold)
        self.assertEqual(node,node2)
    
    def test_not_eq(self):
        node = TextNode("This is a test node", text_type_bold)
        node2 = TextNode("This is a test node", text_type_italic)
        self.assertNotEqual(node,node2)
    
    def test_url_eq(self):
        node = TextNode("This is a test node", text_type_bold,"www.test.com")
        node2 = TextNode("This is a test node", text_type_bold,"www.test.com")
        self.assertEqual(node,node2)
    
    def test_url_not_eq(self):
        node = TextNode("This is a test node", text_type_bold,"www.test.com")
        node2 = TextNode("This is a test node", text_type_bold,"www.test2.com")
        self.assertNotEqual(node,node2)
    
    def test_eq_text(self):
        node = TextNode("This is a test node", text_type_bold)
        node2 = TextNode("This is a test node", text_type_bold)
        self.assertEqual(node,node2)
    
    def test_not_eq_text(self):
        node = TextNode("This is a test node", text_type_bold)
        node2 = TextNode("This is another test node", text_type_bold)
        self.assertNotEqual(node,node2)

if __name__ == "__main__":
    unittest.main()