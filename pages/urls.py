from django.urls import path
from .views import users, new, category

urlpatterns = [
    path('', users, name = 'users'),
    path('new/', new, name = 'new'),
    
    path('category/', category, name='category'), #type:ignore
]
