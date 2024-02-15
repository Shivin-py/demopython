from django import forms

from .models import Item, ReviewRating


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'poster', 'desc', 'category', 'release_date', 'actors', 'trailer_link']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)  # Get the current user from view kwargs
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.user = self.user  # Set the user
        if commit:
            instance.save()
        return instance


class MovieReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewRating
        fields = ['rating', 'review']
        widgets = {
            'rating': forms.NumberInput(attrs={'placeholder': 'Enter your rating in 1 - 5)'}),
            'review': forms.Textarea(attrs={'placeholder': 'Write your review here...'}),
        }

    def clean_rating(self):
        rating = self.cleaned_data['rating']
        if rating < 1.0 or rating > 5.0:
            raise forms.ValidationError("Rating must be between 1 and 5")
        return rating
