import os
import re

def ReadFile(file_path):

    #TODO: Sense box 'float = right' option and specifiy sidebox-right

    with open(file_path) as f:
        lines = list(f)

    # concat each element into a super string
    content = ""
    for l in lines:
        content += l


    return content

def FileName(file_path):

    # returns file name of input file
    file_name = os.path.basename(file_path)

    if file_name.endswith('.mw'):
        file_name = file_name[:-3]

    return file_name

def GetTitle(file_path):

    # returns title from file name and removes unwanted characters
    # update characters to remove as necessiary
    title = os.path.basename(file_path)

    if title.endswith('.mw'):
        title = title[:-3]

    # replace underscores with spaces
    title =  re.sub(r'_', ' ', title)

    return title

def GetBreadcrumb(file_path):

    # returns breadcrumb from the title
    breadcrumb = os.path.basename(file_path)

    if breadcrumb.endswith('.mw'):
        breadcrumb = breadcrumb[:-3]

    # replace underscores with spaces
    breadcrumb =  re.sub(r'_', ' ', breadcrumb)

    return breadcrumb

def GetCategories(file_path):

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

def ProcessFile(file_path, str_content):

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
    content_tmp = ReplaceText('Notice', 'info-box', content_tmp)
    content_tmp = ReplaceText('Warning', 'warning-box', content_tmp)
    content_tmp = ReplaceText('Box', 'sidebox-right', content_tmp)
    
    print("processing " + str(FileName(file_path))+ ".mw...")

    return content_tmp

def ReplaceText(old_text, new_text, str_content):

    # replace old element calls to new element calls
    str_content = re.sub(r'{% include ' + old_text, r'{% include ' + new_text, str_content)

    return str_content

def AddFrontMatter(str_content, file_path):

    # scrap necessary info fom page and populate the front matter.
    title = GetTitle(file_path)
    breadcrumb = GetBreadcrumb(file_path)
    author = "test author"
    categories = GetCategories(file_path)
    description = "test description"
    front_matter_content = "---\ntitle: {0}\nbreadcrumb: {1}\nlayout: page\nauthor: {2}\ncategories: {3}\ndescription: {4}\n---\n\n{5}".format(title, breadcrumb, author, categories, description, str_content)

    return front_matter_content

def WriteFile(file_content, file_path):

    # write file out
    save_path = "/home/edward/Documents/Development/Repos/LOCI/imagej.github.io/pages/"
    file_name = "test.mw"
    complete_name = os.path.join(save_path, file_name)
    title = FileName(file_path)

    with open(complete_name, 'w') as f:

        for e in file_content:
            f.write(e)

        f.close()

    return None

input_file = "/home/edward/Documents/Workspaces/imagej-net-conversion/imagej_mediawiki_source/3D_Viewer.mw"
#input_file = "/home/edward/Documents/Workspaces/imagej-net-conversion/imagej_mediawiki_source/Architecture.mw"
file_contents = ReadFile(input_file)
results = ProcessFile(input_file, file_contents)
results = AddFrontMatter(results,  input_file)
WriteFile(results, input_file)