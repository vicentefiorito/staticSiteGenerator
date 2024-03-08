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
