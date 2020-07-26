import re

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.http import HttpResponse

import markdown2 as markdown

def list_entries():
    """
    Returns a list of all names of encyclopedia entries.
    """
    _, filenames = default_storage.listdir("entries")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))


def save_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    """
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))


def get_entry(title):
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.
    """
    try:
        f = default_storage.open(f"entries/{title}.md")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return None

def md_to_html(file_name):
    '''
    Function that converts markdown to HTML to be rendered to the template.

    Args:
        file_name: (str) the name of the file to be converted

    Returns: 
        The converted code in HTML.
    '''

    markdowner = markdown.Markdown()
    # get the markdown file
    try:
        f = get_entry(file_name)
    except:
        f = f'{file_name} not found!'
    return markdowner.convert(f)


def search_for_file(request, title):
    file_name = ""
    entries = list_entries()
    if title.casefold() not in (entry.casefold() for entry in entries):
        # If page is not valid, render the 404 page.
        context = {
            "name": title,
        }
        return render(request, "encyclopedia/page_not_found.html", context)
    else:
        # If valid, attach the entry name to be used in the rendering of the url
        for entry in entries:
            if entry.casefold() == title:
                file_name = entry
    
    return file_name
