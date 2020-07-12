import os
import re

txt_include_start = "%AA%"
txt_param_start = "%BB%"
txt_param_end = "%CC%"
txt_param_var_start = "%DD%"
txt_liquid_end = "%FF%"
txt_liquid_linebreak_end = "%GG%"
txt_capture_start = "%HH%"
txt_capture_start_end = txt_liquid_linebreak_end
txt_capture_end = "%JJ%"

template_regex = r'(((?<=\n)[ ]*)*(?<!<nowiki>)\{\{[\n ]*([A-Za-z0-9_]*)[ \n]*\|?[ \n]*(([\s\S]*?))\}\})'
template_parameter_regex = r'(\w+([ ]\w+)*)[ ]*=[ ]*([^|]*)'
include_regex = r'((\n )*\{\%[\n ]*include\ ([^\ \n]*)([^\%]*)\%\})'
include_shadowed_regex = r'(' + txt_include_start + '.+?(?=(' + txt_liquid_linebreak_end + '|' + txt_liquid_end + '))(' + txt_liquid_linebreak_end + '|' + txt_liquid_end + '))'
link_with_vertical_bar_regex = r'(\[\[[^\]]*\|[^\]]*\]\])'

global_shadows = [
    ("{% include ", txt_include_start),
    ("=\'", txt_param_start),
    ("=", txt_param_var_start),
    ("\'", txt_param_end),
    ("%}", txt_liquid_end),
    ("%}\n", txt_liquid_linebreak_end),
    ("\n{% endcapture %}\n", txt_capture_end),
    ("\n{% capture ", txt_capture_start),
    ("\n%}\n", txt_capture_end)
]

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
                         r'' + txt_include_start + 'youtube url' + txt_param_start + 'https://www.youtube.com/embed/\1' + txt_param_end + txt_liquid_end, content_tmp)
    content_tmp = re.sub(r'{{[\\]*#widget:Vimeo\|[^}]*}}', r'TODO VIMEO WIDGET', content_tmp)
    # TODO parse flash template?!, removing for now because it creates liquid issues
    content_tmp = re.sub(r'{{[\\]*#widget:flash\|[^}]*}}', r'TODO FLASH WIDGET', content_tmp)
    # TODO parse google spreadsheet template, removing for now because it creates liquid issues
    content_tmp = re.sub(r'{{[\\]*#widget:Google Spreadsheet[ \n]*\|[^}]*}}', r'TODO GOOGLE SPREADSHEET WIDGET', content_tmp)
    # TODO parse SWITCHtube template, removing for now because it creates liquid issues
    content_tmp = re.sub(r'{{[\\]*#widget:SWITCHtube\|[^}]*}}', r'TODO GOOGLE SPREADSHEET WIDGET', content_tmp)

    # replace '{{ stuff }}' mediawiki syntax with '{% include stuff %}` liquid
    content_tmp = replace_template(content_tmp)

    #convert image links into working links - this can be improved, it should not run on all File: links..
    content_tmp = re.sub(r'\[\[File\:([^ |]*)[ ]*\|[ ]*([^x ][^ |]*)[ ]*\|[ ]*link=(?!http)([^\]]*)[ ]*\]\]',
                         r'<a href="\3"><img src="\1" width="\2"/></a>', content_tmp)
    content_tmp = re.sub(r'\[\[File\:([^ |]*)[ ]*\|[ ]*x([^ |]*)[ ]*\|[ ]*link=([^\]]*)\]\]',
                         r'<a href="\3"><img src="\1" height="\2"/></a>', content_tmp)

    content_tmp = re.sub(r'\[\[File\:([^ |]*)[ ]*\|[ ]*link=([^\]]*)[ ]*\|[ ]*([^x ][^ |]*)[ ]*\]\]',
                         r'[[File:\1 |\3|link=\2 ]]', content_tmp)

    content_tmp = content_tmp.replace("{{-}}", "")
    content_tmp = content_tmp.replace("{{}}", "")
    content_tmp = content_tmp.replace("{{!}}", "")

    return content_tmp


def reveal_includes(content_tmp):
    for real, shadow in global_shadows:
        content_tmp = content_tmp.replace(shadow, real)
    return content_tmp


def replace_template(document_content):
    # loop over the template pattern
    pattern = re.compile(template_regex)
    for match in re.findall(pattern, document_content):
        template_full = match[0]
        template_name = match[2]
        template_content = match[3]
        document_content, found_sub = replace_template_match(document_content, template_full, template_name, template_content)
        if found_sub:
            # in the template was another template and got replaced
            # we start the template patter matching loop again to match based on the updated content
            return replace_template(document_content)
    return document_content


def replace_template_match(document_content, match_content, template_name, template_content):
    # first check if another template is in the content of the matched template
    content_remove_first_bracket = match_content.strip()[2:]
    pattern = re.compile(template_regex)
    found_sub_template = False
    for match in re.findall(pattern, content_remove_first_bracket):
        # inside template found, try to convert it..
        _content = replace_template_match(document_content, match[0], match[2], match[3])[0]
        if not _content == document_content:
            document_content = _content
            found_sub_template = True
    if found_sub_template:
        return document_content, True

    # correct template names with spaces
    template_name = fix_template_name(template_name)
    template_content.strip()

    if len(template_name) < 2 or template_name.isdigit():
        # not a template
        return document_content, False

    if len(template_content) == 0:
        return document_content.replace(match_content, txt_include_start + template_name + txt_liquid_linebreak_end), False

    # handle inline templates
    template_content = re.sub(r'\'', r'"', template_content)
    if template_name == "bc":
        document_content = document_content.replace(match_content,
                                                    txt_include_start + template_name + " content" + txt_param_start + cleanup(template_content) + txt_param_end + txt_liquid_end)
    else:
        matched_parameters, captures = match_content_parameters(template_content)
        if len(captures) > 0:
            document_content = document_content.replace(match_content, captures +
                                                    txt_include_start + template_name + " " + matched_parameters + txt_liquid_end)
        else:
            document_content = document_content.replace(match_content,
                                                    txt_include_start + template_name + " " + matched_parameters + txt_liquid_end)
    return document_content, False


def fix_template_name(name):
    name = name.strip().replace(" ", "-")
    name = name.replace("_", "-")
    name = name.lower()
    name = name.replace('notice', 'info-box')
    name = name.replace('infobox', 'info-box')
    name = name.replace('warning', 'warning-box')
    # name = name.replace('box', 'sidebox-right')
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
    include_pattern = re.compile(include_shadowed_regex)
    shadows_include = []
    shadows_links = []
    idx = 0
    for match in re.findall(include_pattern, template_content):
        idx += 1
        shadow = "___SHADOW" + str(idx) + "___"
        shadows_include.append((shadow, match[0]))
        template_content = template_content.replace(match[0], shadow)

    # links with vertical bars make it hard to convert the parameters, so we are shadowing them too
    link_with_vertical_bar_pattern = re.compile(link_with_vertical_bar_regex)
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
    for (key, unused, value) in re.findall(parameter_pattern, template_content):
        value = value.strip()
        # [URL] are not converted, and since it has no title, the brackets are not needed in markdown
        value = re.sub(r'\[(http[^ \]]*)\]', r'\1', value)
        value = re.sub(r'(\[(\[\[[^\]]*\]\])?[ ]*(http[^\]]*)\])', r' \1 ', value)
        pattern_matched = True
        key = key.replace(" ", "-")
        if key == "1":
            key = "content"
        # if there were includes in the value of a parameter, capture the content
        if any(s[0] in value for s in shadows_include):
            captures += txt_capture_start + key + txt_capture_start_end + value + txt_capture_end
            res += key + txt_param_var_start + key + " "
        else:
            res += key + txt_param_start + cleanup(value) + txt_param_end + " "

    # check if additionally to having parameters, the template has an unnamed value as well,
    # e.g. {{template this is the unnamed value|x=bla|y=blub}}
    # if yes, attach as `content`
    if pattern_matched:
        match = re.match(r'^([^\|\=]*)\|', template_content)
        if match:
            content = match[1].strip()
            if len(content) > 0:
                res = "content" + txt_param_start + content + txt_param_end + " " + res
    else:
        # if we are shadowing includes, capture the content of the parameter, otherwise liquid breaks
        if any(s[0] in template_content for s in shadows_include):
            captures += txt_capture_start + " content " + txt_capture_start_end + template_content + txt_capture_end
            res = "content" + txt_param_var_start + "content "
        else:
            content = cleanup(template_content).strip()
            if len(content.strip()) > 0:
                res = "content" + txt_param_start + content + txt_param_end + " "
    # unshadow includes and links
    for shadow, include in shadows_include:
        captures = captures.replace(shadow, include)
    for shadow, link in shadows_links:
        res = res.replace(shadow, link)
    # print(res)
    return res, captures


def cleanup(value):
    return value
    # return " ".join(value.replace("\n", " ").split())


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

        # print(processed_mw)

        run_pandoc(tmp_file, path_out)
        os.remove(tmp_file)

        # open output file and create list
        content_tmp = read_file(path_out)

        # do replacements in md format
        content_tmp = reveal_includes(content_tmp)
        content_tmp = re.sub(r'<http(.*)>', r'http\1', content_tmp)
        content_tmp = re.sub(r'<img src=\"(?!http)([^\"]*)\"', r'<img src="/images/pages/\1"', content_tmp)
        content_tmp = re.sub(r'(\!\[[^\]]*\]\()([^"\)]*[ \n]\"[^\"]*\"[ ]*\))', r'\1/images/pages/\2"', content_tmp)

        # pattern = re.compile(include_regex)
        # for match in re.findall(pattern, content_tmp):
        #     content_tmp = content_tmp.replace(match[0], cleanup(match[0]))

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
    os.system('pandoc {0} -f mediawiki -t gfm --wrap=none -s -o {1}'.format(path_in, path_out))
