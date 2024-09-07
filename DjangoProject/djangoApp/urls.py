from django.urls import path
from . import views

# localhost:8000/djangoApp/items
urlpatterns = [
    path('items/', views.items, name='Items'),
    path('<int:framework_id>/', views.framework_details, name='framework_details'),
 
]
    