from htmlnode import ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node

# types of markdown blocks
block_type_paragraph = 'paragraph'
block_type_heading = 'heading'
block_type_code = 'code'
block_type_quote = 'quote'
block_type_unordered_list = 'unordered_list'
block_type_ordered_list = 'ordered_list'

# this function takes raw Markdown strings as inputs
# returns a list of "block" strings
def markdown_to_blocks(markdown):
    block_strings = []
    strings = markdown.split('\n\n')
    for string in strings:
        string = string.strip()
        block_strings.append(string)
    return block_strings

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = [] 
    for block in blocks:
        html_node = block_to_html(block)
        children.append(html_node)
    return ParentNode('div',children,None)

# this function takes an specific type of blocks
# and calls the specific function for the type of block
def block_to_html(block):
    block_type = block_to_block_type(block)
    if block_type == block_type_paragraph:
        return paragraph_to_html_node(block)
    if block_type == block_type_code:
        return code_to_html_node(block)
    if block_type == block_type_heading:
        return heading_to_html_node(block)
    if block_type == block_type_quote:
        return quote_to_html_node(block)
    if block_type == block_type_ordered_list:
        return ordered_list_to_html_node(block)
    if block_type == block_type_unordered_list:
        return unordered_list_to_html_node(block)
    raise ValueError('Invalid block type!')

# function that takes a single block of markdwon and return the type of block it is
def block_to_block_type(block):
    # this splits the block between opening quotes and closing quotes
    lines = block.split('\n\n')

    if (
        block.startswith('#')
        or block.startswith('##') 
        or block.startswith('###')
        or block.startswith('####')
        or block.startswith('#####')
        or block.startswith('######')
        ):
        return block_type_heading
    
    if len(lines) > 0 and lines[0].startswith('```') and lines[-1].startswith('```'):
        return block_type_code
    
    if block.startswith('>'):
        for line in lines:
            if not line.startswith('>'):
                return block_type_paragraph
        return block_type_quote
    
    if block.startswith('*'):
        for line in lines:
            if not line.startswith('*'):
                return block_type_paragraph
        return block_type_unordered_list
    if block.startswith('-'):
        for line in lines:
            if not line.startswith('-'):
                return block_type_paragraph
        return block_type_unordered_list

    if block.startswith("1."):
        i = 1
        for line in lines:
            if not line.startswith(f'{i}.'):
                return block_type_paragraph
            i += 1
        return block_type_ordered_list
    
    return block_type_paragraph

# helper function that converts inline elements 
# into html nodes to be processed by other functions
def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children

def paragraph_to_html_node(block):
    lines = block.split('\n')
    paragraph = "".join(lines)
    children = text_to_children(paragraph)
    return ParentNode('p',children)

def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == '#':
            level += 1
        else:
            break
    if level + 1 > len(block):
        raise ValueError('Invalid header level: ${level}')
    text = block[level + 1:]
    children = text_to_children(text)
    return ParentNode(f'h{level}',children)

def code_to_html_node(block):
    if not block.startswith('```') or not block.endswith('```'):
        raise ValueError('Invalid code block')
    text = block[4:-3]
    children = text_to_children(text)
    code = ParentNode('code',children)
    return ParentNode('pre',[code])

def unordered_list_to_html_node(block):
    items = block.split('\n')
    children_nodes = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        children_nodes.append(ParentNode('li',children))
    return ParentNode('ul',children_nodes)

def ordered_list_to_html_node(block):
    items = block.split('\n')
    children_nodes = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        children_nodes.append(ParentNode('li',children))
    return ParentNode('ol',children_nodes)

def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)