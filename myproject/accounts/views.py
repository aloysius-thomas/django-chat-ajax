from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from accounts.forms import UserCreateForm
from accounts.models import User


def create_user(request):
    title = "Create User"
    form = UserCreateForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(f'/user/{instance.id}/info')
    context = {
        'title': title,
        'form': form,
    }
    return render(request, 'accounts/user_form.html', context)


def user_info(request, user_id=None):
    instance = get_object_or_404(User, id=user_id)

    context = {
        'instance': instance,
    }
    return render(request, 'accounts/user_info.html', context)

