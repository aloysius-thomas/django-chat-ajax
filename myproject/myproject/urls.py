from django.contrib import admin
from django.urls import include
from django.urls import path
from home import views as home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.home, name='home'),
    path('user/', include('accounts.urls')),
]
