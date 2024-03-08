import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
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