from django import forms


class PublishForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control publish-post', 'rows':2, 'cols':45, 'placeholder': 'Publish new post'}), max_length=260)
    image = forms.ImageField()