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
    