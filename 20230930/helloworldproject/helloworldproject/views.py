from django.http import HttpResponse
from django.views.generic import TemplateView

def helloworldfunc(request):
    responceobject = HttpResponse("<h1>hello world<h1>")
    return responceobject


class HelloworldClass(TemplateView):
    template_name = "hello.html"
