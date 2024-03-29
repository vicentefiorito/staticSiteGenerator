class HTMLNode:
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError('to_html method not implemented correctly')
    
    def props_to_html(self):
        # if there is no props in the node just return empty
        if self.props is None:
            return ""
        # else, loop throught the dict and add every piece to a final string
        prop_string = ""
        for prop in self.props:
            prop_string += f' {prop}="{self.props[prop]}"'
        return prop_string

    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'

# LeafNode, a HTMLNode with no children
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError('All leaf nodes require a value')
        if self.tag is None:
            return self.value
        
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
    
    def __repr__(self):
        return f'LeafNode({self.tag},{self.value}.{self.props})'

# ParentNode, a HTMLNode responsible for nesting the HTMLNodes inside of one another to create HTML strings
# Any HTMLNode that's not a LeafNode, is a ParentNode
class ParentNode(HTMLNode):
    def __init__(self, tag,children, props=None):
        super().__init__(tag, None, children, props)
    
    # recursive method
    def to_html(self):
        # base case
        if self.tag is None:
            raise ValueError('tag was not provided')
        if self.children is None:
            raise ValueError('All parent node require children')
        
        # recursive case
        parent_str = f'<{self.tag}{self.props_to_html()}>'
        for child in self.children:
            parent_str += f'{child.to_html()}'
        parent_str += f'</{self.tag}>'
        
        return parent_str

    def __repr__(self):
        return f'ParentNode({self.tag},{self.children},{self.props})'