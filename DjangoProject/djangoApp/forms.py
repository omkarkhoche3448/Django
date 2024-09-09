from django import forms
from .models import Framework_Reviews

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Framework_Reviews
        fields = ['review', 'rating']
        widgets = {
            'review': forms.Textarea(attrs={'rows': 4, 'class': 'w-full p-2 border border-gray-300 rounded'}),
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5, 'class': 'w-20 p-2 border border-gray-300 rounded'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['review'].label = 'Your Review'
        self.fields['rating'].label = 'Rating (out of 5)'
