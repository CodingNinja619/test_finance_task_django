from django import forms

from .models import Category, Status, SubCategory, Type, Transaction


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

class TransactionAdminForm(forms.ModelForm):

    class Meta:
        model = Transaction
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance and self.instance.pk:
            if self.instance.type:
                self.fields["category"].queryset = Category.objects.filter(type_id=self.instance.type.id)
            
            if self.instance.category:
                self.fields["subcategory"].queryset = SubCategory.objects.filter(category_id=self.instance.category.id)
        else:
            # при создании — ничего не показываем (или всё)
            self.fields["category"].queryset = Category.objects.none()
            self.fields["subcategory"].queryset = SubCategory.objects.none()
        # maybe else next