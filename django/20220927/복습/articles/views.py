from django.shortcuts import render
from .models import Articles

# Create your views here.
def root(request):

    guestbook = Articles.objects.all()

    return render(request, "root.html", {"guestbook": guestbook})


def create(request):
    Articles.objects.create(content=request.GET["long"])
    return render(request, "create.html", {"text": request.GET["long"]})
