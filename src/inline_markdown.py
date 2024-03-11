from textnode import (
    text_type_text,
    text_type_bold,
    text_type_link,
    text_type_code,
    text_type_image,
    text_type_italic,
    TextNode
)

def split_nodes_delimiter(old_nodes,delimeter,text_type):
    # this is the list that is going to return after the delimeter
    new_nodes = []
    for old_node in old_nodes:
        if not isinstance(old_node,TextNode):
            new_nodes.append(old_node)
        # flag to keep track of the text type
        is_original_text_type = True
        phrases = old_node.text.split(delimeter)
        # this checks for the edge case where there is no closing delimeter
        if len(phrases) % 2 != 0:
            raise ValueError('Unmatched delimeter found in text.')
        for phrase in phrases:
            if is_original_text_type:
                word = TextNode(phrase,old_node.text_type)
            else:
                word = TextNode(phrase,text_type)
            is_original_text_type = not is_original_text_type
            new_nodes.append(word)
    return new_nodes

    