from django import forms

RATING_CHOICES = (('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'))


class TestimonialForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                         'placeholder': 'NAME'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control',
                                                            'placeholder': 'E-MAIL'}))
    rating = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), choices=RATING_CHOICES)
    comment = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',
                                                           'placeholder': 'REVIEW'}))
    # name = forms.CharField()
    # email = forms.EmailField()
    # rating = forms.ChoiceField()
    # comment = forms.CharField()
