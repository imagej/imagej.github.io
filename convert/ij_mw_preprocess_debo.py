import os
import re

inline_blocks = ["citation", "cite"]

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


template_regex = r'(\{\{[\n ]*([A-Za-z0-9_]*)[ \n]*\|?[ \n]*(([\s\S]*?))\}\})'
template_parameter_regex = r'([a-z]+)[ ]*=[ ]*([^|]*)'
include_regex = r'(\{\%[\n ]*include\ ([^\ \n]*)(.*)\%\})'
link_with_vertical_bar_regex = r'(\[\[[^\]]*\|[^\]]*\]\])'


def process_file(str_content):

    # perform regex replacements
    content_tmp = str_content

    # remove unused sidebox details
    # content_tmp = re.sub(r'title[ \n]=[ \n]', '', content_tmp)
    # content_tmp = re.sub(r'\|[ \n]width = (.*)\n', '', content_tmp)
    # content_tmp = re.sub(r'\|[ \n]float = (.*)\n', '', content_tmp)
    # content_tmp = re.sub(r'\|[ \n]text =', '', content_tmp)

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
    content_tmp = replace_template(content_tmp)

    #convert image links into working links - this can be improved, it should not run on all File: links..
    content_tmp = re.sub(r'\[\[File\:([^ |]*)[ ]*\|[ ]*([^x ][^ |]*)[ ]*\|[ ]*link=(?!http)(.*)[ ]*\]\]',
                         r'<a href="\3"><img src="\1" width="\2"/></a>', content_tmp)
    content_tmp = re.sub(r'\[\[File\:([^ |]*)[ ]*\|[ ]*x([^ |]*)[ ]*\|[ ]*link=(.*)[ ]*\]\]',
                         r'<a href="\3"><img src="\1" height="\2"/></a>', content_tmp)

    return content_tmp


def replace_template(document_content):
    # loop over the template pattern
    pattern = re.compile(template_regex)
    for match in re.findall(pattern, document_content):
        template_full = match[0]
        template_name = match[1]
        template_content = match[2]
        document_content, found_sub = replace_template_match(document_content, template_full, template_name, template_content)
        if found_sub:
            # in the template was another template and got replaced
            # we start the template patter matching loop again to match based on the updated content
            return replace_template(document_content)
    return document_content


def replace_template_match(document_content, match_content, template_name, template_content):
    # first check if another template is in the content of the matched template
    content_remove_first_bracket = match_content[2:]
    pattern = re.compile(template_regex)
    found_sub_template = False
    for match in re.findall(pattern, content_remove_first_bracket):
        # inside template found, try to convert it..
        _content = replace_template_match(document_content, match[0], match[1], match[2])[0]
        if not _content == document_content:
            document_content = _content
            found_sub_template = True
    if found_sub_template:
        return document_content, True

    # correct template names with spaces
    template_name = fix_template_name(template_name)
    template_content.strip()

    if len(template_name) == 1 or template_name.isdigit():
        # not a template
        return document_content, False

    if len(template_content) == 0:
        return document_content.replace(match_content, "{% include " + template_name + " %}"), False

    if template_name not in inline_blocks:
        # handle inline templates
        template_content = re.sub(r'\'', r'"', template_content)
        if template_name == "bc":
            document_content = document_content.replace(match_content,
                                                        "{% include " + template_name + " content=\'" + template_content + "\'%}")
        else:
            matched_parameters, captures = match_content_parameters(template_content)
            if len(captures) > 0:
                document_content = document_content.replace(match_content, captures +
                                                        "{% include " + template_name + " " + matched_parameters + "%}")
            else:
                document_content = document_content.replace(match_content,
                                                        "{% include " + template_name + " " + matched_parameters + "%}")
    else:
        document_content = document_content.replace(match_content,
                                                    "\n{% capture includecontent %}\n" + template_content + "\n{% endcapture %}\n"
                                                    "\n{% include " + template_name + " content=includecontent %}\n")
    return document_content, False


def fix_template_name(name):
    name = name.strip().replace(" ", "-")
    name = name.replace("_", "-")
    name = name.lower()
    name = name.replace('notice', 'info-box')
    name = name.replace('infobox', 'info-box')
    name = name.replace('warning', 'warning-box')
    name = name.replace('box', 'sidebox-right')
    name = name.replace('info-sidebox-right', 'sidebox-right')
    name = name.replace('key-press', 'key')
    name = name.replace('biglink', 'big-link')
    name = name.replace('bignotice', 'big-notice')
    name = name.replace('developmenu', 'develop-menu')
    name = name.replace('expandingbox', 'expanding-box')
    name = name.replace('githubembed', 'github-embed')
    name = name.replace('importingclasses', 'importing-classes')
    name = name.replace('listofupdatesites', 'list-of-update-sites')
    name = name.replace('personlist', 'person-list')
    name = name.replace('userbox', 'user-box')
    name = name.replace('componentstats', 'component-stats')
    name = name.replace('updatesitesmenu', 'menu-updatesites')
    name = name.replace('cookbookmenu', 'menu-cookbook')
    name = name.replace('licensesmenu', 'menu-licenses')
    name = name.replace('platformsmenu', 'menu-platforms')
    name = name.replace('formatsmenu', 'menu-formats')
    name = name.replace('helpmenu', 'menu-help')
    return name


def match_content_parameters(template_content):
    # in case there are already converted includes in the template content, it messes with converting the parameters,
    # so we shadow them with a numbered string and put them back in after converting the parameters.
    include_pattern = re.compile(include_regex)
    link_with_vertical_bar_pattern = re.compile(link_with_vertical_bar_regex)
    shadows_include = []
    shadows_links = []
    idx = 0
    for match in re.findall(include_pattern, template_content):
        idx += 1
        shadow = "___SHADOW" + str(idx) + "___"
        shadows_include.append((shadow, match[0]))
        template_content = template_content.replace(match[0], shadow)

    for match in re.findall(link_with_vertical_bar_pattern, template_content):
        idx += 1
        shadow = "___SHADOW" + str(idx) + "___"
        shadows_links.append((shadow, match))
        template_content = template_content.replace(match, shadow)

    parameter_pattern = re.compile(template_parameter_regex)
    pattern_matched = False
    res = ""
    captures = ""
    # check if template has parameters, e.g. is of form `x=bla|y=blub`
    for (key, value) in re.findall(parameter_pattern, template_content):
        value = value.strip()
        pattern_matched = True
        # if there were includes in the value of a parameter, capture the content
        if any(s[0] in value for s in shadows_include):
            captures += "\n{% capture " + key + " %}\n" + value + "\n{% endcapture %}\n"
            res += key + "=" + key + " "
        else:
            res += key + "=\'" + value + "\' "
    # check if additionally to having parameters, the template has an unnamed value as well,
    # e.g. {{template this is the unnamed value|x=bla|y=blub}}
    # if yes, attach as `content`
    if pattern_matched:
        match = re.match(r'^([^\|\=]*)\|', template_content)
        if match:
            res = "content=\'" + match[1].strip() + "\' " + res
    else:
        if any(s[0] in template_content for s in shadows_include):
            captures += "\n{% capture content %}\n" + template_content + "\n{% endcapture %}\n"
            res = "content=content "
        else:
            res = "content=\'" + template_content + "\' "
    for shadow, include in shadows_include:
        captures = captures.replace(shadow, include)
    for shadow, link in shadows_links:
        res = res.replace(shadow, link)
    return res, captures


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
        processed_mw = process_file(read_file(path_in))
        tmp_file = os.path.join(os.path.dirname(path_out), "tmpconversionfile.mw")
        write_file(processed_mw, tmp_file)

        run_pandoc(tmp_file, path_out)
        os.remove(tmp_file)

        # open output file and create list
        content_tmp = read_file(path_out)

        # do replacements in md format
        content_tmp = re.sub(r'<http(.*)>', r'http\1', content_tmp)
        content_tmp = re.sub(r'<img src=\"(?!http)([^\"]*)\"', r'<img src="/images/pages/\1"', content_tmp)
        content_tmp = re.sub(r'(\!\[[^\]]*\]\()([^"\)]*[ \n]\"[^\"]*\"[ ]*\))', r'\1/images/pages/\2"', content_tmp)

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
