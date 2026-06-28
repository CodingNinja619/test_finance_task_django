from django import forms

from .models import Category, Status, SubCategory, Type


class TransactionFilterForm(forms.Form):
    date_from = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            "type": "date",
            "id": "date_from",
            "class": "form-control",
        })
    )
    date_to = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            "type": "date",
            "id": "date_to",
            "class": "form-control",
        }),
    )
    status = forms.ModelChoiceField(
        queryset=Status.objects.all(),
        required=False,
        empty_label="Все",
        widget=forms.Select(attrs={
            "class": "form-select",
        }),
    )
    type = forms.ModelChoiceField(
        queryset=Type.objects.all(),
        required=False,
        empty_label="Все",
        widget=forms.Select(attrs={
            "id": "type-select",
            "class": "form-select",
        }),
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
        empty_label="Все",
        widget=forms.Select(attrs={
            "id": "category-select",
            "class": "form-select",
            "disabled": True,
        }),
    )
    subcategory = forms.ModelChoiceField(
        queryset=SubCategory.objects.all(),
        required=False,
        empty_label="Все",
        widget=forms.Select(attrs={
            "id": "subcategory-select",
            "class": "form-select",
            "disabled": True,
        }),
    )
    min_amount = forms.DecimalField(
        required=False,
        widget=forms.NumberInput(attrs={
            "class": "form-control",
            "placeholder": "0",
        }),
    )
    max_amount = forms.DecimalField(
        required=False,
        widget=forms.NumberInput(attrs={
            "class": "form-control",
            "placeholder": "10000",
        }),
    )
    comment = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Поиск по комментариям",
        }),
    )


