from django.shortcuts import render
from .models import ContactInfo

# Create your views here.
def index(request):
    context = {
        "contacts": ContactInfo.objects.all()
    }
    return render(request, "contact/index.html", context)