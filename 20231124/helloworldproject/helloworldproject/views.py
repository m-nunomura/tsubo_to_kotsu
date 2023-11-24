from django.http import HttpResponse

def helloworldfunc(request):
    responseobject = HttpResponse("<h1>helloworld</h1>")
    return responseobject