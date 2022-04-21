from django import forms

class Encurtar(forms.Form):
    url_original = forms.URLField(max_length=100, widget=forms.URLInput(attrs={"class":"form-control","placeholder":"url para encurtar", })) 