from django.contrib import admin
from django.urls import path
from DJproject.views import user_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', user_view),
]
