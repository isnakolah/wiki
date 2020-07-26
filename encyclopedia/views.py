from django.shortcuts import render
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


def view_page(request, title):
    '''
    Function that renders the page based on the title entered on the url.

    Args:
        title: (str) string written on the url

    Returns:
        page_not_found render if the page is not there OR renders the page with the given title
    '''
    # entries = util.list_entries()

    # Converting the markdown to html to render to page

    file_name = util.search_for_file(request, title)

    content = util.md_to_html(file_name) 

    return render(request, "encyclopedia/view_page.html", {
        "content": content,
        "name": file_name,
    })