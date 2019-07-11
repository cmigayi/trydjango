from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
	title = forms.CharField(
			widget=forms.TextInput(
					attrs={
						"placeholder": "Product title:"
					}
				)
		)
	desc = forms.CharField(
			widget=forms.Textarea(
					attrs={
						"placeholder": "Product description:",
						"rows": 5,
						"colums": 20,
					}
				)
		)
	price = forms.DecimalField() 

	class Meta: 
		model = Product
		fields = [
			"title",
			"desc",
			"price"
		]

	def clean_title(self, *args, **kwargs):
		title = self.cleaned_data.get("title")
		if len(title) > 5:
			print("You crazy jo!")
		else:
			raise forms.ValidationError("Title has less words")

		return title			


class RawProductForm(forms.Form):
	title = forms.CharField(
			widget=forms.TextInput(
					attrs={
						"placeholder": "Product title:"
					}
				)
		)
	desc = forms.CharField(
			widget=forms.Textarea(
					attrs={
						"placeholder": "Product description:",
						"rows": 5,
						"colums": 20,
					}
				)
		)
	price = forms.DecimalField()