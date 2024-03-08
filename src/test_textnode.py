import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a test node", "bold")
        node2 = TextNode("This is a test node", "bold")
        self.assertEqual(node,node2)
    
    def test_not_eq(self):
        node = TextNode("This is a test node", "bold")
        node2 = TextNode("This is a test node", "italic")
        self.assertNotEqual(node,node2)
    
    def test_url_eq(self):
        node = TextNode("This is a test node", "bold","www.test.com")
        node2 = TextNode("This is a test node", "bold","www.test.com")
        self.assertEqual(node,node2)
    
    def test_url_not_eq(self):
        node = TextNode("This is a test node", "bold","www.test.com")
        node2 = TextNode("This is a test node", "bold","www.test2.com")
        self.assertNotEqual(node,node2)
    
    def test_eq_text(self):
        node = TextNode("This is a test node", "bold")
        node2 = TextNode("This is a test node", "bold")
        self.assertEqual(node,node2)
    
    def test_not_eq_text(self):
        node = TextNode("This is a test node", "bold")
        node2 = TextNode("This is another test node", "bold")
        self.assertNotEqual(node,node2)

if __name__ == "__main__":
    unittest.main()