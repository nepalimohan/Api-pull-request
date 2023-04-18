from django.urls import path
from .views import users, new, category, category_post

urlpatterns = [
    path('', users, name = 'users'),
    path('new/', new, name = 'new'),
    
    path('category/', category, name='category'), #type:ignore
    path('category_post/', category_post, name='category_post'), #type:ignore
]
