from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('blogs', blogs, name='blogs'),
    path('category_blogs/<str:slug>/', category_blogs, name='category_blogs'),

]
