from django.urls import path
from . import views

urlpatterns = [
    path('items/', views.items, name='Items'),
    path('<int:framework_id>/', views.framework_details, name='framework_details'),
    path('enroll/<int:course_id>/', views.enroll_confirmation, name='enroll_confirmation'),
    path('enroll_course/<int:course_id>/', views.enroll_course, name='enroll_course'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    path('course/<int:course_id>/review/', views.submit_review, name='submit_review'),
]
