from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.WatchData),
    path('admin/', admin.site.urls),
    path('fetch',views.FetchData),

]