from django import forms
import authuser.models as users
import budgetcategory.models as budget


class CreateEntryForm(forms.Form):
    name = forms.CharField(label='name')
    date = forms.DateField(label='setDate')
    targetValue = forms.IntegerField(label='balance')


class EditEntryForm(forms.Form):
    targetValue = forms.IntegerField(label='balance')
