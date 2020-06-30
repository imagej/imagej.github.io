import os
import re

def read_file(file_path):

    #TODO: Sense box 'float = right' option and specifiy sidebox-right

    with open(file_path) as f:
        lines = list(f)

    # concat each element into a super string
    content = ""
    for l in lines:
        content += l


    return content

def get_name(file_path):

    # returns file name of input file
    name = os.path.basename(file_path)

    if name.endswith('.mw'):
        name = name[:-3]

    return name

def get_title(file_path):

    # returns title from file name and removes unwanted characters
    # update characters to remove as necessiary
    title = os.path.basename(file_path)

    if title.endswith('.mw'):
        title = title[:-3]

    # replace underscores with spaces
    title =  re.sub(r'_', ' ', title)

    return title

def get_breadcrumb(file_path):

    # returns breadcrumb from the title
    breadcrumb = os.path.basename(file_path)

    if breadcrumb.endswith('.mw'):
        breadcrumb = breadcrumb[:-3]

    # replace underscores with spaces
    breadcrumb =  re.sub(r'_', ' ', breadcrumb)

    return breadcrumb

def get_categories(file_path):

    # Reads the bottom of the file, finds categories and returns the formated front matter "categories".
    categories = []

    with open(file_path) as f:
        for line in f:
            try:
                x = re.search(r'\[\[Category:(.*?)\]\]', line).group(1)
                categories.append(x)
            except:
                pass

    str_categories = ""
    for n in categories:
        str_categories += n + ","

    str_categories = str_categories[:-1]

    return str_categories

def process_file(file_path, str_content):

    # perform regex replacements
    content_tmp = str_content

    # remove unused sidebox details
    content_tmp = re.sub(r'title[ \n]=[ \n]', '', content_tmp)
    content_tmp = re.sub(r'\|[ \n]width = (.*)\n', '', content_tmp)
    content_tmp = re.sub(r'\|[ \n]float = (.*)\n', '', content_tmp)
    content_tmp = re.sub(r'\|[ \n]text =', '', content_tmp)

    # replace '{{ stuff }}' mediawiki syntax with '{% include stuff %}` liquid
    content_tmp = re.sub(r'{{[ \n]*([A-Za-z0-9_]*)[ \n]*\|[ \n]*([^}]*)[ \n]*}}',r'{% include \1 content="\2" %}' ,content_tmp)
    content_tmp = re.sub(r'{{[ \n]*([A-Za-z0-9_]*)[ \n]*}}', r'%Replace% \1 %Replace% ', content_tmp)
    content_tmp = replace_text('Notice', 'info-box', content_tmp)
    content_tmp = replace_text('Warning', 'warning-box', content_tmp)
    content_tmp = replace_text('Box', 'sidebox-right', content_tmp)
    
    print("processing " + str(get_name(file_path))+ ".mw...")

    return content_tmp

def replace_text(old_text, new_text, str_content):

    # replace old element calls to new element calls
    str_content = re.sub(r'{% include ' + old_text, r'{% include ' + new_text, str_content)

    return str_content

def add_front_matter(str_content, file_path):

    # scrap necessary info fom page and populate the front matter.
    title = get_title(file_path)
    breadcrumb = get_breadcrumb(file_path)
    author = "test author"
    categories = get_categories(file_path)
    description = "test description"
    front_matter_content = "---\ntitle: {0}\nbreadcrumb: {1}\nlayout: page\nauthor: {2}\ncategories: {3}\ndescription: {4}\n---\n\n{5}".format(title, breadcrumb, author, categories, description, str_content)

    return front_matter_content

def write_file(file_content, file_path):

    # write file out
    save_path = "/home/edward/Documents/Development/Repos/LOCI/imagej.github.io/pages/"
    file_name = "test.mw"
    complete_name = os.path.join(save_path, file_name)

    with open(complete_name, 'w') as f:

        for e in file_content:
            f.write(e)

        f.close()

    return None

def run_pandoc(file_path):
    
    stream = os.popen('pwd')
    output = stream.read()
    print("This is the output: " + output)
    
    return None


path = "/home/edward/Documents/Workspaces/imagej-net-conversion/imagej_mediawiki_source/3D_Viewer.mw"
#path = "/home/edward/Documents/Workspaces/imagej-net-conversion/imagej_mediawiki_source/Architecture.mw"
file_contents = read_file(path)
output = process_file(path, file_contents)
run_pandoc()
write_file(output, path)

# generate front matter and add to post-pandoc file
fm = add_front_matter(file_contents, path)