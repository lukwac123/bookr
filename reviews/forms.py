from django import forms

SEARCH_CHOICES = (("title", "Tytuł"),
                  ("contributor", "Współtwórca"))

class SearchForm(forms.Form):
    search = forms.CharField(required=False, min_length=3)
    search_in = forms.ChoiceField(required=False, choices=SEARCH_CHOICES)
