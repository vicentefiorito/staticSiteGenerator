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
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        # list to take the slipt nodes of every node
        split_node = []
        phrases = old_node.text.split(delimeter)
        # this checks for the edge case where there is no closing delimeter
        if len(phrases) % 2 == 0:
            raise ValueError('Unmatched delimeter found in text.')
        for i in range(len(phrases)):
            if phrases[i] == "":
                continue
            if i % 2 == 0:
                split_node.append(TextNode(phrases[i],text_type_text))
            else:
                split_node.append(TextNode(phrases[i],text_type))
        new_nodes.extend(split_node)
    return new_nodes

    