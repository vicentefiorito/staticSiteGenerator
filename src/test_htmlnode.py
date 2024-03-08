import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    # HTML node simple tests
    def test_html_node(self):
        node = HTMLNode("div","This is a div with text inside",None,{"class":"index","href":"google.com"})
        nodeProps = node.props_to_html()
        expectedProps = ' class="index" href="google.com"'
        self.assertEqual(nodeProps,expectedProps)
    
    def test_html_node2(self):
        node = HTMLNode("p","this is a paragraph with text",None,{"class":"p-class","target":"blank"})
        nodeProps = node.props_to_html()
        expectedProps = ' class="p-class" target="blank"'
        self.assertEqual(nodeProps,expectedProps)

    # Leaf Node tests
    def test_leaf_node_no_tag(self):
        node = LeafNode(None,"This is a p element with no tag")
        nodeProps = node.to_html()
        expectedProps = 'This is a p element with no tag'
        self.assertEqual(nodeProps,expectedProps)
    
    def test_leaf_node(self):
        node = LeafNode('h1', "This is an H1 div")
        nodeProps = node.to_html()
        expectedProps = '<h1>This is an H1 div</h1>'
        self.assertEqual(nodeProps,expectedProps)

    def test_leaf_node_with_props(self):
        node = LeafNode('h1', "This is an H1 div",{'class':'container'},)
        nodeProps = node.to_html()
        expectedProps = '<h1 class="container">This is an H1 div</h1>'
        self.assertEqual(nodeProps,expectedProps)

if __name__ == "__main__":
    unittest.main()