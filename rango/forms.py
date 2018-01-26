from django import forms
from rango.models import Page, Category

class CategoryForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(CategoryForm, self).__init__(*args, **kwargs)

		self.fields["name"].help_text = "Please enter the category name."

	class Meta:
		model = Category
		fields = ("name",)

class PageForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(PageForm, self).__init__(*args, **kwargs)

		self.fields["title"].help_text = "Please enter the title of the page."
		self.fields["url"].help_text = "Please enter the URL of the page."

	class Meta:
		model = Page
		fields = ("title", "url")

	def clean(self):
		cleaned_data = self.cleaned_data
		url = cleaned_data.get("url")
		if url and not url.startswith("http://") and not url.startswith("https://"):
			url = "http://" + url
			cleaned_data["url"] = url

			return cleaned_data
