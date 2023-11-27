from django.http import HttpResponse
from django.views import generic

def helloworldfunc(request):
    responseobject = HttpResponse("<h1>hello world</h1>")
    return responseobject

class HelloWorldClass(generic.TemplateView):
    template_name = "hello.html"
    