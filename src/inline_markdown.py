import re

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

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError('Invalid Markdown, image tag was not closed!')
            if sections[0] != "":
                 new_nodes.append(TextNode(sections[0],text_type_text))
            new_nodes.append(TextNode(image[0],text_type_image,image[1]))
            original_text = sections[1]
        if original_text == "":
            new_nodes.append(TextNode(original_text,text_type_text))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"![{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError('Invalid Markdown, link tag was not closed!')
            if sections[0] != "":
                 new_nodes.append(TextNode(sections[0],text_type_text))
            new_nodes.append(TextNode(link[0],text_type_link,link[1]))
            original_text = sections[1]
        if original_text == "":
            new_nodes.append(TextNode(original_text,text_type_text))
    return new_nodes

# takes raw text and return a list of tuples,
# each tuple has the alt text and the URL of any markdown image
def extract_markdown_images(text):
    # regex to find the image
    pattern = r"!\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern,text)
    return matches

# takes raw text and return a list of tuples,
# each tuple has the anchor text and the URL
def extract_markdown_links(text):
    pattern = r"\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern,text)
    return matches

    