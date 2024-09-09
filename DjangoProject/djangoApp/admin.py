from django.contrib import admin
from .models import FrameWork_Varity, Framework_Reviews, Framework_courses, FrameWork_certificate,EnrolledCourse

# Register the models with the Django admin site
@admin.register(FrameWork_Varity)
class FrameWork_VarityAdmin(admin.ModelAdmin):
    list_display = ('name', 'framework_type', 'date_time')
    search_fields = ('name', 'framework_type')
    list_filter = ('framework_type',)

@admin.register(Framework_courses)
class Framework_coursesAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'framework', 'course_duration', 'course_price')
    search_fields = ('course_name', 'course_description')
    list_filter = ('framework',)

@admin.register(Framework_Reviews)
class Framework_ReviewsAdmin(admin.ModelAdmin):
    list_display = ('user', 'framework', 'rating', 'date_time')
    search_fields = ('user__username', 'review')
    list_filter = ('rating',)

@admin.register(FrameWork_certificate)
class FrameWork_certificateAdmin(admin.ModelAdmin):
    list_display = ('certificate_name', 'user', 'framework', 'certificate_number')
    search_fields = ('certificate_name', 'certificate_description', 'certificate_number')
    list_filter = ('framework', 'user')

@admin.register(EnrolledCourse)
class EnrolledCourseAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'enrollment_date')
    search_fields = ('user__username', 'course__course_name')
