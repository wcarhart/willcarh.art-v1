from django import forms

class EmailForm(forms.Form):
	name = forms.CharField(
		max_length=100,
		widget=forms.TextInput(attrs={
			"id": "form_name",
			"type": "text",
			"name": "name",
			"class": "form-control",
			"placeholder": "What's your name?",
			"required": "required"
		})
	)

	email = forms.CharField(
		max_length=100,
		widget=forms.TextInput(attrs={
			"id": "form_email",
			"type": "email",
			"name": "email",
			"class": "form-control",
			"placeholder": "What's your email?",
			"required": "required"
		})
	)

	message = forms.CharField(
		widget=forms.Textarea(attrs={
			"id": "form_message",
			"name": "message",
			"class": "form-control",
			"placeholder": "What's up?",
			"rows": "4",
			"required": "required"
		})
	)
