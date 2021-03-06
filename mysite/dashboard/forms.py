from django import forms

from food.models import Category, Product


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(
                attrs={'class': 'form-control'},
            )
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        widgets = {
            "title": forms.TextInput(
                attrs={'class': 'form-control'},
            ),
            "description": forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            "price": forms.NumberInput(
                attrs={'class': 'form-control'},
            ),
            "category": forms.Select(
                attrs={'class': 'form-control'},
            )
        }
