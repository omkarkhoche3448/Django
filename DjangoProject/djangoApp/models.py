from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

class FrameWork_Varity(models.Model):  
    FRAMEWORK_TYPE_CHOICE = [
        ("React", "JavaScript"),
        ("Next.js", "TypeScript"),
        ("Django", "Python"),
        ("Angular.js", "TypeScript"),
    ]

    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='djangoApp/images')
    date_time = models.DateTimeField(default=timezone.now)
    framework_type = models.CharField(
        max_length=50, choices=FRAMEWORK_TYPE_CHOICE, default="React"
    )
    description = models.TextField(default='')
    documentation_url = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})


# One-to-many relationship: Framework has many reviews
class Framework_Reviews(models.Model):  
    framework = models.ForeignKey(FrameWork_Varity, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField(default='')
    rating = models.IntegerField(default=0)
    date_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Review by {self.user.username} on {self.framework.name}'


# Many-to-one relationship: Framework can have many courses
class Framework_courses(models.Model):  
    framework = models.ForeignKey(FrameWork_Varity, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=50)
    course_description = models.TextField(default='')
    course_duration = models.CharField(max_length=50)
    course_price = models.CharField(max_length=50)
    course_image = models.ImageField(upload_to='djangoApp/images')
    course_url = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.course_name


# One-to-many relationship: Framework can have many certificates
class FrameWork_certificate(models.Model):  
    framework = models.ForeignKey(FrameWork_Varity, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    certificate_name = models.CharField(max_length=50)
    certificate_number = models.CharField(max_length=50)
    certificate_description = models.TextField(default='')
    certificate_image = models.ImageField(upload_to='djangoApp/images')
    certificate_url = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return f'{self.certificate_name} - {self.user.username}'
