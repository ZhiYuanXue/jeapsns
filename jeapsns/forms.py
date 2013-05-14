from django import forms

class PuForm(forms.Form):
	name    = forms.CharField()
	address = forms.CharField()
	city    = forms.CharField()

class PuForm(forms.Form):
    username    = forms.CharField()
    image = forms.CharField()
    text =  forms.CharField(laber="",widget=forms.Textarea)

