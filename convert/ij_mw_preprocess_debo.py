import os
import re
import regex
import sys
import codecs

txt_include_start = "%AA%"
txt_param_start = "%BB%"
txt_param_end = " %CC%"
txt_param_end2 = "%CC%"
txt_param_var_start = "%DD%"
txt_liquid_end = "%FF%"
txt_liquid_linebreak_end = "%GG%"
txt_capture_start = "%HH%"
txt_capture_start_end = txt_liquid_linebreak_end
txt_capture_end = "%JJ%"
txt_youtube = "%KK%"
txt_single_quote = "%LL%"
txt_newline = "%MM"
txt_apply_style_start = "%NN%"
txt_apply_style_end = "%OO%"
txt_colon = "%PP%"
txt_colon2 = "%QQ%"

template_regex = r'(((?<=\n)[ ]*)*(?<!<nowiki>)\{\{[\n ]*([A-Za-z0-9_]*)[ \n]*\:?\|?[ \n]*(([\s\S]*?))\}\})'
template_parameter_regex = r'(\w+([ ]\w+)*)[ ]*=[ ]*([^|]*)'
include_regex = r'((\n )*\{\%[\n ]*include\ ([^\ \n]*)([^\%]*)\%\})'
include_shadowed_regex = r'(' + txt_include_start + '.+?(?=(' + txt_liquid_linebreak_end + '|' + txt_liquid_end + '))(' + txt_liquid_linebreak_end + '|' + txt_liquid_end + '))'
link_with_vertical_bar_regex = r'(\[\[[^\]]*\|[^\]]*\]\])'

fix_math = ["Ops Deconvolution"]

global_shadows = [
    ("{% include ", txt_include_start),
    ("=\'", txt_param_start),
    ("=", txt_param_var_start),
    ("\'", txt_param_end),
    ("\'", txt_param_end2),
    ("%}", txt_liquid_end),
    ("%}\n", txt_liquid_linebreak_end),
    ("\n{% endcapture %}\n", txt_capture_end),
    ("\n{% capture ", txt_capture_start),
    ("\n%}\n", txt_capture_start_end),
    ("https://www.youtube.com/embed/", txt_youtube),
    ("\\\'", txt_single_quote),
    (":", txt_colon),
    (";", txt_colon2),
    ("\n", txt_newline)
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
    breadcrumb =  re.sub(r':', ' ', breadcrumb)

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

    content_tmp = re.sub(r'\_\_FORCETOC\_\_[ ]?', r'', content_tmp)
    content_tmp = re.sub(r'\_\_TOC\_\_[ ]?', r'', content_tmp)
    content_tmp = re.sub(r'\_\_NOTOC\_\_[ ]?', r'', content_tmp)

    # fix youtube template
    content_tmp = re.sub(r'\{\{[\\]?\#widget\:YouTube\|id\=([^ \|]*)[^\}]*\}\}',
                         youtube_match, content_tmp)
    content_tmp = re.sub(r'\{\{[\\]?\#widget\:YouTube\|playlist\=([^ \|]*)[^\}]*\}\}',
                         youtube_playlist_match, content_tmp)
    content_tmp = re.sub(r'{{[\\]*#widget:Vimeo\|[^}]*}}', r'TODO VIMEO WIDGET', content_tmp)
    # TODO parse flash template?!, removing for now because it creates liquid issues
    content_tmp = re.sub(r'{{[\\]*#widget:flash\|[^}]*}}', r'TODO FLASH WIDGET', content_tmp)
    # TODO parse google spreadsheet template, removing for now because it creates liquid issues
    content_tmp = re.sub(r'{{[\\]*#widget:Google Spreadsheet[ \n]*\|[^}]*}}', r'TODO GOOGLE SPREADSHEET WIDGET', content_tmp)
    # TODO parse SWITCHtube template, removing for now because it creates liquid issues
    content_tmp = re.sub(r'{{[\\]*#widget:SWITCHtube\|[^}]*}}', r'TODO GOOGLE SPREADSHEET WIDGET', content_tmp)

    content_tmp = re.sub(r'\<gallery\>[ \n]*([^\<]*(?!\<\/gallery\>)*)\<\/gallery\>', gallery_match, content_tmp)

    # fix file links - since they are also stacked, this needs to happen recursively
    content_tmp = regex.sub(r'\[((?>[^\[\]]+|(?R))*)\]', file_match, content_tmp)

    # replace '{{ stuff }}' mediawiki syntax with '{% include stuff %}` liquid
    content_tmp = replace_template(content_tmp)

    content_tmp = content_tmp.replace("{{-}}", "")
    content_tmp = content_tmp.replace("{{}}", "")
    content_tmp = content_tmp.replace("{{!}}", "")

    # fix tables
    # - keep row style
    content_tmp = re.sub(r'\{\|style=\"([^\n]+)\"[ ]*\n([^\n]+)', match_table_header, content_tmp)
    content_tmp = re.sub(r'(\||\!) style=\"([^\"]*)\"[ ]*\|', match_table_row_style, content_tmp)
    # - fix colspan - add additional columns to make pandoc not skip table content
    content_tmp = re.sub(r'(\!|\|) colspan=(\d*)[ ]*(?:style\=\"([^\"]*)\")?(?:[ ]*\|([^\n]*))\n', match_table_colspan, content_tmp)
    content_tmp = re.sub(r'\n(\||\!)(.*(?:' + txt_include_start + ')+.*)', r'\n\1<span><br/></span>\2', content_tmp)

    # fix math - keeping the math tags makes
    content_tmp = content_tmp.replace("<math>", "$$")
    content_tmp = content_tmp.replace("</math>", "$$")

    # print(content_tmp)
    return content_tmp


def match_table_header(match):
    return txt_apply_style_start + shadow(match.group(1)) + txt_apply_style_end + '\n{|\n' + match.group(2)


def match_table_row_style(match):
    return match.group(1) + txt_apply_style_start + shadow(match.group(2)) + txt_apply_style_end


def match_table_colspan(match):
    emptycols = ''
    for i in range(int(match.group(2))-1):
        emptycols += '|\n'
    return match.group(1) + match.group(4) + '\n' + emptycols


def shadow(text):
    shadowed = text.replace(";", txt_colon2)
    shadowed = shadowed.replace(":", txt_colon)
    return shadowed


def youtube_match(match):
    return txt_include_start + 'youtube url' + txt_param_start + txt_youtube + match.group(1) + txt_param_end + txt_liquid_end


def youtube_playlist_match(match):
    return txt_include_start + 'youtube-playlist url' + txt_param_start + txt_youtube + match.group(1) + txt_param_end + txt_liquid_end


def gallery_content_match(gallery_content):
    imgs = re.findall(r'([^\n|]*)\|caption\|([^\n]*)', gallery_content)
    res = ""
    for match in imgs:
        path = match[0]
        if path.startswith("File:"):
            filename = path.replace('File:', '')
            filename = filename[0].capitalize() + filename[1:]
            path = '/media/' + filename
        res += path + ' | ' + match[1] + txt_newline
    return res[:-len(txt_newline)]


def gallery_match(match):
    capture = txt_capture_start + 'content' + txt_capture_start_end + gallery_content_match(match.group(1)) + txt_capture_end
    return capture + txt_include_start + 'gallery content' + txt_param_var_start + 'content' + txt_liquid_linebreak_end;


def file_match(match):
    res = re.sub(r'^\[\[(?:Image|File)[ ]*:([^|]*)\|[ ]*thumb[ ]*\|(.*)\]\]$', fix_thumbnail_match, match[0])
    res = re.sub(r'^\[\[(?:Image|File)[ ]*\:([^ |]*)[ ]*\|[ ]*([^x ][^ |]*)[ ]*\|[ ]*link=([^\]]*)[ ]*\]\]$',
                         fix_src_width_link_match, res)
    res = re.sub(r'^\[\[(?:Image|File)[ ]*\:([^ |]*)[ ]*\|[ ]*link=([^\]]*)\|[ ]*([^x ][^ |]*)[ ]*[ ]*\]\]$',
                         fix_src_link_width_match, res)
    res = re.sub(r'^\[\[(?:Image|File)[ ]*\:([^ |]*)[ ]*\|[ ]*link=([^\]]*)\|[ ]*(x[^ |]*)[ ]*[ ]*\]\]$',
                         fix_src_link_height_match, res)
    res = re.sub(r'^\[\[(?:Image|File)[ ]*\:([^ |]*)[ ]*\|[ ]*x([^ |]*)[ ]*\|[ ]*link=([^\]]*)\]\]$',
                         fix_src_height_link_match, res)

    res = re.sub(r'^\[\[(?:Image|File)[ ]*\:([^ |]*)[ ]*\|[ ]*thumb[ ]*\|[ ]*([^|]*)[ ]*\]\]$',
                         fix_thumbnail_match, res)

    res = re.sub(r'^\[\[(?:Image|File)[ ]*\:([^ |]*)[ ]*\|([\d]*)px[ ]*\]\]$',
                         fix_src_width_match, res)

    res = re.sub(r'^\[\[(?:Image|File)[ ]*\:[ ]*([^ |]*)[ ]*\|(?:right\||left\||center\|)?([\d]*)px[ ]*\]\]$',
                         fix_src_width_match, res)

    res = re.sub(r'^\[\[(?:Image|File)[ ]*\:[ ]*([^ |]*)[ ]*\|(?:right\||left\||center\|)?x([\d]*)px[ ]*\]\]$',
                         fix_src_height_match, res)

    res = re.sub(r'^\[\[(?:Image|File)[ ]*\:([^ |]*)[ ]*\|\|([ ]*[^\]]*[ ]*)\]\]$',
                         fix_simple_image_match, res)

    res = re.sub(r'^\[\[File\:([^ |]*)[ ]*\|[ ]*link=([^\]]*)[ ]*\|[ ]*([^x ][^ |]*)[ ]*\]\]$',
                         r'[[File:\1 |\3|link=\2 ]]', res)

    res = re.sub(r'\[\[[ ]*wikipedia[ ]*:[ ]*(http[^\|]*\|[^\]]*\]\])', r'[[\1', res)
    res = re.sub(r'\[\[[ ]*wikipedia[ ]*:([^\|]*)\|([^\]]*)\]\]', wikipedia_match, res)

    return res


def wikipedia_match(match):
    res = txt_include_start + 'wikipedia title' + txt_param_start + match.group(1) \
          + txt_param_end + ' text' + txt_param_start + match.group(2) + txt_param_end + txt_liquid_end
    return res.replace("\'", txt_single_quote)


def fix_simple_image_match(match):
    return fix_simple_image(match.group(1), match.group(2))


def fix_simple_image(src, title):
    return "[[File:" + fix_image_name(src) + "|" + title + "]]"


def fix_thumbnail_match(match):
    return fix_thumbnail(match.group(1), match.group(2))


def fix_thumbnail_match2(match):
    return fix_thumbnail(match.group(1), match.group(3))


def fix_thumbnail(src, title):
    title = replace_template(title)
    title = regex.sub(r'\[((?>[^\[\]]+|(?R))*)\]', file_match, title)
    title = re.sub(r'(?:right\||left\||center\|)?([x]?\d*px\|)?(?:right\||left\||center\|)?((?:.*|\n)*)$', r'\2', title)
    if title.startswith("link="):
        link = re.sub(r'^link\=[\[]?([^|]*)[\]]?\|((?:.*|\n)*)$', r'\2', title)
        title = re.sub(r'^link\=[^|]*\|((?:.*|\n)*)$', r'\1', title)
        if txt_include_start in title:
            capture = txt_capture_start + 'title' + txt_capture_start_end + title + txt_capture_end
            return capture + txt_include_start + 'thumbnail-link src="/media/' \
                   + fix_image_name(src) + '" title' + txt_param_var_start + 'title ' \
                   + ' link' + txt_param_start + link + txt_param_end + txt_liquid_end
        else:
            title = title.replace("\'", txt_single_quote)
            if txt_include_start in title:
                capture = txt_capture_start + 'title' + txt_capture_start_end + title + txt_capture_end
                return capture + txt_include_start + 'thumbnail-link src="/media/' \
                       + fix_image_name(src) + '" title' + txt_param_var_start + 'title ' \
                       + ' link' + txt_param_start + link + txt_param_end + txt_liquid_end
            else:
                return txt_include_start + 'thumbnail-link src="/media/' \
                       + fix_image_name(src) + '" title' + txt_param_start + title + txt_param_end \
                       + ' link' + txt_param_start + link + txt_param_end + txt_liquid_end
    else:
        if txt_include_start in title:
            capture = txt_capture_start + 'title' + txt_capture_start_end + title + txt_capture_end
            return capture + txt_include_start + 'thumbnail src' + txt_param_start + '/media/' \
                   + fix_image_name(src) + txt_param_end + ' title' + txt_param_var_start + 'title ' + txt_liquid_end
        else:
            title = title.replace("\'", txt_single_quote)
            return txt_include_start + 'thumbnail src' + txt_param_start + '/media/' \
                   + fix_image_name(
                src) + txt_param_end + ' title' + txt_param_start + title + txt_param_end + txt_liquid_end


def fix_image_name(src):
    src = src[0].capitalize() + src[1:]
    return src.replace("_", " ")


def fix_src_width_match(match):
    return fix_src_width(match.group(1), match.group(2))


def fix_src_height_match(match):
    return fix_src_height(match.group(1), match.group(2))


def fix_src_width_link_match(match):
    return fix_src_link_width(match.group(1), match.group(3), match.group(2))


def fix_src_link_width_match(match):
    return fix_src_link_width(match.group(1), match.group(2), match.group(3))


def fix_src_link_height_match(match):
    return fix_src_link_height(match.group(1), match.group(2), match.group(3))


def fix_src_height_link_match(match):
    return fix_src_link_height(match.group(1), match.group(3), match.group(2))


def fix_src_width(src, width):
    return '<img src="' + fix_image_name(src) + '" width="' + width + '"/>'


def fix_src_link_width(src, link, width):
    return '<a href="' + link + '"><img src="' + fix_image_name(src) + '" width="' + width + '"/></a>'


def fix_src_height(src, height):
    return '<img src="' + fix_image_name(src) + '" height="' + height + '"/>'


def fix_src_link_height(src, link, height):
    return '<a href="' + link + '"><img src="' + fix_image_name(src) + '" height="' + height + '"/></a>'


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

    # filter out {{}}, {{1}}, {{-}} etc.
    if len(template_name) < 2 or template_name.isdigit():
        return document_content, False

    if len(template_content) == 0:
        return document_content.replace(match_content, txt_include_start + template_name + txt_liquid_linebreak_end), False

    # handle inline templates
    template_content = re.sub(r'\'', r'"', template_content)
    if template_name == "bc":
        color_match = re.match(r'color=([\w]*)\|', template_content)
        if color_match:
            template_content = re.sub(r'color=[\w]*\|(.*)', r'\1', template_content)
            document_content = document_content.replace(match_content,
                                                        txt_include_start + template_name + " content" + txt_param_start + cleanup(template_content) + txt_param_end
                                                        + " color" + txt_param_start + color_match[1] + txt_param_end + txt_liquid_end)
        else:
            document_content = document_content.replace(match_content,
                                    txt_include_start + template_name + " content" + txt_param_start + cleanup(
                                    template_content) + txt_param_end + txt_liquid_end)
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
    title = title.replace(":", " ›")
    title = title.replace("%2F", "/")
    breadcrumb = get_breadcrumb(file_path)
    breadcrumb = breadcrumb.replace("%2F", "/")
    categories = get_categories(file_path)
    description = "test description"
    front_matter_content = "---\ntitle: {0}\nbreadcrumb: {1}\nlayout: {2}\ncategories: {3}\ndescription: {4}\n---\n\n{5}".format(title, breadcrumb, layout, categories, description, str_content)

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

        # print(content_tmp)

        # do replacements in md format

        # bring all shadowed includes back
        content_tmp = reveal_includes(content_tmp)

        # fix <http://imagej.net> links
        content_tmp = re.sub(r'<(http.*)>', r'\1', content_tmp)
        # fix escaped | in breadcrumb include
        content_tmp = re.sub(r'(\{\% include bc content)(.+?)(?=\%\})', fix_bc_include, content_tmp)
        # fix internal links
        content_tmp = re.sub(r'((?<!\!)\[[^\]]*\]\()((?!#)(?!http)(?!mailto\:)(?:[^\)\"]|(?:\\\)))*)([.]*(?:\"[^\"]*\")?(?<!\\)\))', fix_link_match, content_tmp)
        # fix internal image src paths
        content_tmp = re.sub(r'<img src=\"(?!http)(?!/media/)([^\"]*)\"', fix_img_image, content_tmp)
        content_tmp = re.sub(r'((?<!-)\!\[(?!\[)[^\]]*\]\()((?!http)(?!\/media\/)[^\"\)]*)([ \n]*(?:\"[^\"]*\")?[ ]*\))', fix_md_image, content_tmp)
        # remove empty html tags I guess?!
        content_tmp = re.sub(r'\<span\>[ \n]*\<br[ ]*\/\>[ \n]*\<\/span\>', r'', content_tmp)
        # reapply table row styles
        content_tmp = re.sub(r'(\<td|\<th)(\>.*?(?=' + txt_apply_style_start + '))' + txt_apply_style_start + '(.+?)(?=' + txt_apply_style_end + ')' + txt_apply_style_end, r'\1 style="\3"\2', content_tmp)
        content_tmp = re.sub(r'\| ' + txt_apply_style_start + '(.+?)(?=' + txt_apply_style_end + ')' + txt_apply_style_end, r'|', content_tmp)
        content_tmp = re.sub(r'' + txt_apply_style_start + '([^\n]*)' + txt_apply_style_end + '[\n ]*(<\w*)', r'\2 style="\1"', content_tmp)
        # remove empty paragraph tags
        content_tmp = re.sub(r'\<p\>\<\/p\>', r'', content_tmp)
        # remove left over styles which could not be attached to any HTML tag
        content_tmp = re.sub(r'\n' + txt_apply_style_start + '.*' + txt_apply_style_end, r'', content_tmp)
        # fix math
        content_tmp = re.sub(r'\$\$(.+?)(?=\$\$)\$\$', fix_converted_math, content_tmp)
        if title in fix_math:
            content_tmp = re.sub(r'\n(\$\$.*\$\$)\n', r'\n{% raw %}\1{% endraw %}\n', content_tmp)

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


def fix_converted_math(match):
    res = re.sub(r'(?<!\\)\\', r'', match.group(1))
    return '$$' + res + '$$'


def fix_bc_include(match):
    return match.group(1) + match.group(2).replace("\|", "|")


def fix_link_match(match):
    if match.group(1).startswith('[File:'):
        # return '![/media/' + match.group(2)
        return match.group(0)
    if match.group(1).startswith('[Category:'):
        return ''
    link = match.group(2).replace(":Category", "Category")
    link = link.replace(":", "_").replace("\'", "").replace("\"", "").replace("\(", "").replace("\)", "").replace("/", "_")
    link = link[0].capitalize() + link[1:].rstrip()
    return match.group(1) + link + match.group(3).replace("\"wikilink\"", "")


def fix_md_image(match):
    if ".pdf" in match.group(0):
        media_name = fix_image_name(match.group(2)).rstrip()
        return "[" + media_name + "](/media/" + media_name + ")"
    return match.group(1) + "/media/" + fix_image_name(match.group(2)) + match.group(3)


def fix_img_image(match):
    return '<img src="/media/' + fix_image_name(match.group(1)) + '"'


def run_pandoc(path_in, path_out):
    os.system('pandoc {0} -f mediawiki -t gfm --wrap=none -s -o {1}'.format(path_in, path_out))
