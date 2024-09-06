from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class FrameWork_Varity(models.Model):
    FrameWork_TYPE_CHOICE = [
        ("React", "Javacript"),
        ("Next.js", "Typescript"),
        ("Django", "Python"),
        ("Angular.js", "Typescript")
    ]

    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='djangoApp/images')
    date_time = models.DateTimeField(default=timezone.now)
    framework_type = models.CharField(max_length=50, choices=FrameWork_TYPE_CHOICE,default="Reacts")
    description = models.TextField(default='')
    documentation_url = models.URLField(max_length=200, blank=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
