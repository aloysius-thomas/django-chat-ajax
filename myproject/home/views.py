from django.shortcuts import redirect
from django.shortcuts import render

from accounts.models import User


def home(request):
    users = User.objects.all().exclude(id=request.user.id)
    context = {
        'users': users
    }
    return render(request, "home/home.html", context)
