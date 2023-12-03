from django import forms

class MoveForm(forms.Form):
    position = forms.IntegerField(min_value=0, max_value=8)