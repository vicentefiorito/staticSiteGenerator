import os
from markdown_blocks import markdown_to_html_node

def extract_title(markdown):
    lines = markdown.split('\n')
    for line in lines:
        if line.startswith('# '):
            return line[2:]
    raise ValueError('No header provided')

def generate_page(from_path, template_path,dest_path):
    print(f'Generating page from {from_path} to {dest_path} using {template_path}')
    from_file = open(from_path,'r')
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path,'r')
    template = template_file.read()
    template_file.close()
    
    # converts the markdown of the from_file to html
    nodes = markdown_to_html_node(markdown_content)
    html = nodes.to_html()

    # extracts the title of the markdown
    title = extract_title(markdown_content)
    template = template.replace('{{Title}}',title)
    template = template.replace('{{Content}}',html)

    # writes the new HTML to a file at dest_path
    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path,exist_ok=True)
    to_file = open(dest_path,'w')
    to_file.write(template)