from django.contrib import admin
from .models import FrameWork_Varity, Framework_Reviews, Framework_courses, FrameWork_certificate

# Registering FrameWork_Varity model
@admin.register(FrameWork_Varity)
class FrameWorkVarityAdmin(admin.ModelAdmin):
    list_display = ('name', 'framework_type', 'date_time')
    search_fields = ('name', 'framework_type')
    list_filter = ('framework_type',)

# Registering Framework_Reviews model
@admin.register(Framework_Reviews)
class FrameworkReviewsAdmin(admin.ModelAdmin):
    list_display = ('framework', 'user', 'rating', 'date_time')
    search_fields = ('framework__name', 'user__username')
    list_filter = ('rating',)

# Registering Framework_courses model
@admin.register(Framework_courses)
class FrameworkCoursesAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'course_duration', 'course_price', 'framework')
    search_fields = ('course_name',)
    list_filter = ('framework',)

# Registering FrameWork_certificate model
@admin.register(FrameWork_certificate)
class FrameWorkCertificateAdmin(admin.ModelAdmin):
    list_display = ('certificate_name', 'user', 'certificate_number', 'framework')
    search_fields = ('certificate_name', 'certificate_number')
    list_filter = ('framework',)
