from django.shortcuts import render
from django.http import HttpResponse
import markdown2 as markdown
from . import util

def index(request):
    '''
    Function that returns the render of the index.hmtl file

    Returns:
        Renders the index page.
    '''
    # for entry in util.get_entry():
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


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
    f = util.get_entry(file_name)
    return markdowner.convert(f)


def verify(title):
    '''
    '''
    entries = util.list_entries()
    # Checking if the title is valid - caseinsensitive
    if title.casefold() not in (entry.casefold() for entry in entries):
        # If page is not valid, render the 404 page.
        return HttpResponse(f"Error 404, Page not found\n{title} page you are looking for cannot be found.")
    else:
        # If valid, attach the entry name to be used in the rendering of the url
        for entry in entries:
            if entry.casefold() == title:
                title_name = entry

    return title_name


def view_page(request, title):
    '''
    Function that renders the page based on the title entered on the url.

    Args:
        title: (str) string written on the url

    Returns:
        page_not_found render if the page is not there OR renders the page with the given title
    '''
    file_name = ""
    entries = util.list_entries()
    # Checking if the title is valid - caseinsensitive
    if title.casefold() not in (entry.casefold() for entry in entries):
        # If page is not valid, render the 404 page.
        return render(request, "encyclopedia/page_not_found.html")
    else:
        # If valid, attach the entry name to be used in the rendering of the url
        for entry in entries:
            if entry.casefold() == title:
                file_name = entry

    # Converting the markdown to html to render to page
    content = md_to_html(file_name)
    return render(request, "encyclopedia/view_page.html", {
        "content": content,
        "name": file_name,
    })
