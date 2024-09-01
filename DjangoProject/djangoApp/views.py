from django.shortcuts import render

# View for localhost:8000/djangoApp/items
def items(request):
    return render(request, 'djangoApp/items.html')
