from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import FrameWork_Varity

# View for localhost:8000/djangoApp/items
def items(request):
    FrameWorks= FrameWork_Varity.objects.all()
    return render(request, 'djangoApp/items.html', {'FrameWorks':FrameWorks })

def framework_details(request, framework_id):
    framework = get_object_or_404(FrameWork_Varity, pk=framework_id)
    return render(request, 'djangoApp/framework_details.html', {'framework': framework})



    