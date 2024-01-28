from django import forms

from catalog.models import Product

class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
class ProductForm(StyleFormMixin,forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

