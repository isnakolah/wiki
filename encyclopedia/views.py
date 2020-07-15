from django.shortcuts import render
import markdown2 as markdown
from . import util

app_name = "encyclopedia"
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def view_page(request, title):
    markdowner = markdown.Markdown()
    file_name = ""
    
    # Checking if the title is valid
    if title.casefold() not in (entry.casefold() for entry in util.list_entries()):
        return render(request, "encyclopedia/page_not_found.html", {
            "name": title
        })
    else:
        for entry in util.list_entries():
            if entry.casefold() == title:
                file_name = entry

    f = util.get_entry(file_name)
    content = markdowner.convert(f)
    return render(request, "encyclopedia/view_page.html", {
        "content": content,
        "name": title
    })

