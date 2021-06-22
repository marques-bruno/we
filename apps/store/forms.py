from django import forms
from django.forms import ModelForm

from .store_models import Product

class ProductForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        ## add a "form-control" class to each form input
        ## for enabling bootstrap
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })

    class Meta:
        model = Product
        fields = ('__all__')
        widgets = {'birthdate': forms.DateInput(attrs={'type':'date'}),
                   'labels': forms.CheckboxSelectMultiple,
                   'allergens': forms.CheckboxSelectMultiple,
                   'description': forms.Textarea(attrs={"rows":5, "cols":50}),
                   'farmers_advice': forms.Textarea(attrs={"rows":5, "cols":50}),
                   }
