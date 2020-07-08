import os
import re

misbehaving_includes = ["infobox", "imagej1", "citation", "person", "publication", "javadoc", "github", "tip", "testimonial"]
inline_includes = ["person", "github", "bc", "listofupdatesites", "list-of-update-sites", "key", "key-press", "learn",
                   "project", "clear", "develop-menu", "developmenu", "big-link", "biglink", "path", "inline", "logo", "toc"]

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

    if not file_path:
        return ""

    # returns breadcrumb from the title
    breadcrumb = os.path.basename(file_path)

    if breadcrumb.endswith('.mw'):
        breadcrumb = breadcrumb[:-3]

    # replace underscores with spaces
    breadcrumb =  re.sub(r'_', ' ', breadcrumb)

    return breadcrumb

def get_categories(file_path):

    if not file_path:
        return ""

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


template_regex = r'[ \t]*{{[\n]*([A-Za-z0-9_ ]*)[ \n]*\|[ \n]*([^}]*)[ \n]*}}'


def process_file(file_path, str_content):

    # perform regex replacements
    content_tmp = str_content

    # remove unused sidebox details
    content_tmp = re.sub(r'title[ \n]=[ \n]', '', content_tmp)
    content_tmp = re.sub(r'\|[ \n]width = (.*)\n', '', content_tmp)
    content_tmp = re.sub(r'\|[ \n]float = (.*)\n', '', content_tmp)
    content_tmp = re.sub(r'\|[ \n]text =', '', content_tmp)

    # fix youtube template
    content_tmp = re.sub(r'{{[\\]*#widget:YouTube\|id=([\w\d\-_]*)[a-z=|\d]*}}',
                         r'{% include youtube url="https://www.youtube.com/embed/\1" %} ', content_tmp)
    # TODO parse flash template?!, removing for now because it creates liquid issues
    content_tmp = re.sub(r'{{[\\]*#widget:flash\|[^}]*}}', r'TODO FLASH WIDGET', content_tmp)
    # TODO parse google spreadsheet template, removing for now because it creates liquid issues
    content_tmp = re.sub(r'{{[\\]*#widget:Google Spreadsheet[ \n]*\|[^}]*}}', r'TODO GOOGLE SPREADSHEET WIDGET', content_tmp)
    # TODO parse SWITCHtube template, removing for now because it creates liquid issues
    content_tmp = re.sub(r'{{[\\]*#widget:SWITCHtube\|[^}]*}}', r'TODO GOOGLE SPREADSHEET WIDGET', content_tmp)

    # replace '{{ stuff }}' mediawiki syntax with '{% include stuff %}` liquid
    pos = -1
    while True:
        match = re.search(template_regex, content_tmp)
        if match:
            if match.start() == pos:
                break
            pos = match.start()
            content_tmp = replace_template(content_tmp, match[0], match[1], match[2])
        else:
            break
    content_tmp = re.sub(r'{{[ \n]*([A-Za-z0-9_]*)[ \n]*}}', r'%Replace% \1 %Replace% ', content_tmp)
    content_tmp = replace_text('notice', 'info-box', content_tmp)
    content_tmp = replace_text('infobox', 'info-box', content_tmp)
    content_tmp = replace_text('warning', 'warning-box', content_tmp)
    content_tmp = replace_text('box', 'sidebox-right', content_tmp)
    content_tmp = replace_text('key-press', 'key', content_tmp)
    content_tmp = replace_text('biglink', 'big-link', content_tmp)
    content_tmp = replace_text('bignotice', 'big-notice', content_tmp)
    content_tmp = replace_text('developmenu', 'develop-menu', content_tmp)
    content_tmp = replace_text('expandingbox', 'expanding-box', content_tmp)
    content_tmp = replace_text('githubembed', 'github-embed', content_tmp)
    content_tmp = replace_text('importingclasses', 'importing-classes', content_tmp)
    content_tmp = replace_text('listofupdatesites', 'list-of-update-sites', content_tmp)
    content_tmp = replace_text('personlist', 'person-list', content_tmp)
    content_tmp = replace_text('userbox', 'user-box', content_tmp)

    # TODO figure out what that is supposed to mean (e.g. Script_Parameters.md)
    content_tmp = content_tmp.replace("{{!}}", "")

    print("processing " + str(get_name(file_path))+ ".mw...")

    return content_tmp


def replace_template(document_content, match_content, template_name, template_content):

    # first check if another template is in the content of the matched template
    content_remove_first_bracket = match_content[2:]
    match = re.search(template_regex, content_remove_first_bracket)
    if match:
        # found inside template, replace this first
        return replace_template(document_content, match[0], match[1], match[2])

    # correct template names with spaces
    template_name = template_name.strip().replace(" ", "-")
    template_name = template_name.replace("_", "-")
    template_name = template_name.lower()

    if template_name in misbehaving_includes:
        print("Cannot parse template " + template_name + " at the moment")
        template_content = "TODO"
    if template_name in inline_includes:
        # handle inline templates
        template_content = re.sub(r'\'', r'"', template_content)
        document_content = document_content.replace(match_content,
                                                    "\n{% include " + template_name + " content=\'" + template_content + "\' %}\n")
    else:
        # handle block templates, capture content
        document_content = document_content.replace(match_content,
                                                    "\n{% capture includecontent %}\n" + template_content + "\n{% endcapture %}\n"
                                                    "\n{% include " + template_name + " content=includecontent %}\n")
    return document_content


def replace_text(old_text, new_text, str_content):

    # replace old element calls to new element calls
    str_content = re.sub(r'{% include ' + old_text, r'{% include ' + new_text, str_content)

    return str_content

def add_front_matter(str_content, file_path, layout, title):

    # scrap necessary info fom page and populate the front matter.
    breadcrumb = get_breadcrumb(file_path)
    author = "test author"
    categories = get_categories(file_path)
    description = "test description"
    front_matter_content = "---\ntitle: {0}\nbreadcrumb: {1}\nlayout: {2}\nauthor: {3}\ncategories: {4}\ndescription: {5}\n---\n\n{6}".format(title, breadcrumb, layout, author, categories, description, str_content)

    return front_matter_content

def write_file(file_content, path_out):
    # TODO: Expose current file/save path to `run_pandoc`

    # write file out
    # save_path = "/home/edward/Documents/Development/Repos/LOCI/imagej.github.io/pages/"
    # file_name = "test.mw"
    # complete_name = os.path.join(save_path, file_name)

    with open(path_out, 'w') as f:
        for e in file_content:
            f.write(e)

        f.close()

    return None


autogenerated_line = 'autogenerated: true\n'


def convert(path_in, path_out, layout, title):

    content_tmp = ""
    if path_in:
        processed_mw = process_file(path_in, read_file(path_in))
        tmpFile = os.path.join(os.path.dirname(path_out), "tmpconversionfile.mw")
        write_file(processed_mw, tmpFile)

        run_pandoc(tmpFile, path_out)
        os.remove(tmpFile)

        # open output file and create list
        content_tmp = read_file(path_out)

        # do replacements in md format
        content_tmp = re.sub(r'<http(.*)>', r'http\1', content_tmp)

    front_matter = add_front_matter(content_tmp, path_in, layout, title)

    # rewrite `.md` file with front matter
    with open(path_out, 'w') as f:
        f.write(front_matter)
        f.close()

    with open(path_out, 'r+') as f:
        lines = f.readlines()
        lines[0] = lines[0] + autogenerated_line
        f.seek(0)
        for line in lines:
            f.write(line)
    return None


def run_pandoc(path_in, path_out):
    os.system('pandoc {0} -f mediawiki -t gfm -s -o {1}'.format(path_in, path_out))
