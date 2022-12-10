from django import forms
from django.template.defaultfilters import slugify
from models import *


class BudgetCategory(forms.ModelForm):
    class Meta:
        model = BudgetType
        fields = ('name',)
    
    def save(self):
        if not self.instance.slug:
            self.instance.slug = slugify(self.cleaned_data['name'])
        super(BudgetCategory, self).save()