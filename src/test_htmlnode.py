import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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
    
    # Parent Node tests
    def test_parent_node(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        nodeProps = node.to_html()
        expectedProps = '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>'
        self.assertEqual(nodeProps,expectedProps)
    
    def test_parent_node_no_tag(self):
        node = ParentNode(
            None,
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertRaises(ValueError,node.to_html)
    
    def test_parent_no_children(self):
        node = ParentNode('b',None)
        self.assertRaises(ValueError,node.to_html)
    
    def test_parent_double_tag(self):
        child_node = LeafNode('a','Link Here!')
        parent_node = ParentNode('h1',[child_node])
        parent_HTML = parent_node.to_html()
        expected_HTML = '<h1><a>Link Here!</a></h1>'
        self.assertEqual(parent_HTML,expected_HTML)
    
    def test_parent_triple_tag(self):
        grandchild_node = LeafNode('b','grandchild')
        child_node = ParentNode('span',[grandchild_node])
        parent_node = ParentNode('h1',[child_node])
        parent_HTML = parent_node.to_html()
        exceptedHTML = '<h1><span><b>grandchild</b></span></h1>'
        self.assertEqual(parent_HTML,exceptedHTML)

if __name__ == "__main__":
    unittest.main()