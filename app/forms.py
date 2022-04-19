from django import forms

class Encurtar(forms.Form):
    url_original = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class":"form-control","placeholder":"url para encurtar", "aria-label":"url", "aria-describedby":"basic-addon1"})) 