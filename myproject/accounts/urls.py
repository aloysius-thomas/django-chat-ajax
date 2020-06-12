from django.urls import path

from accounts import views

app_name = 'user'

urlpatterns = [
    path("create/", views.create_user, name='user-create'),
    path("<int:user_id>/info/", views.user_info, name='user-info'),
]
