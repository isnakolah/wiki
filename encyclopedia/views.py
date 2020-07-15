from django.shortcuts import render
import markdown2

from . import util

app_name = "encyclopedia"
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def css(request):
    html = markdown2.markdown_path(util.get_entry(css))
    return render(request, "encyclopedia/css.html", {
        "content": html
    })
