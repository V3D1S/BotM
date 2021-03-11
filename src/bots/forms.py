from django import forms

class UploadBotForm(forms.Form):
	title = forms.CharField(label="Title", max_length=100)
	description = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 20}))
	price = forms.DecimalField(max_digits=5, decimal_places=2)
	file = forms.FileField()
