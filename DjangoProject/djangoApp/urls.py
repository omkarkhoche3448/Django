from django.urls import path
from . import views

# localhost:8000/djangoApp/items
urlpatterns = [
    path('items/', views.items, name='Items'), 
]
