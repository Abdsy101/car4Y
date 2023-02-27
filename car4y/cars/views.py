from django.shortcuts import render
from .models import Car

# Create your views here.
def index(request):
    context = {
        "cars": Car.objects.all()
    }
    return render(request, "cars/index.html", context)