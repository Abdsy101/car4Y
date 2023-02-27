from django.shortcuts import render
from .models import MainPage

# Create your views here.
def index(request):
    context = {
        "page_data": MainPage.objects.all()
    }
    return render(request, "main/index.html", context)