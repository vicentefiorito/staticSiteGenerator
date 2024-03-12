# this function takes raw Markdown strings as inputs
# returns a list of "block" strings
def markdown_to_blocks(markdown):
    block_strings = []
    strings = markdown.split('\n\n')
    for string in strings:
        string = string.strip()
        block_strings.append(string)
    return block_strings
