from django.urls import path
from .views import helloworldfunc

app_name = "helloworldapp"

urlpatterns = [
    path("helloworldapp/",helloworldfunc),
]