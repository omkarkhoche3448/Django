from django.shortcuts import render
from .models import FrameWork_Varity

# View for localhost:8000/djangoApp/items
def items(request):
    FrameWorks= FrameWork_Varity.objects.all()
    return render(request, 'djangoApp/items.html', {'FrameWorks':FrameWorks })





    