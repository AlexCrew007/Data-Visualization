from django.forms import ModelForm
from .models import dataBase
from django import forms

class FilterForm(ModelForm):
    class Meta:
        model=dataBase
        fields=['end_year','topic','sector','region','source','country']

    def __init__(self,*args,**kwargs):
        super(FilterForm,self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})