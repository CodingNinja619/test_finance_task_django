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
        

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = (
            "status",
            "type",
            "category",
            "subcategory",
            "amount",
            "comment",
        )
        widgets = {
            "status": forms.Select(attrs={"class": "form-select"}),
            "type": forms.Select(attrs={"id": "type-select", "class": "form-select"}),
            "category": forms.Select(attrs={"id": "category-select", "class": "form-select"}),
            "subcategory": forms.Select(attrs={"id": "subcategory-select", "class": "form-select"}),
            "amount": forms.NumberInput(attrs={
                "class": "form-control",
                "step": "0.01",
                "placeholder": "0.00",
            }),
            "comment": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3,
                "placeholder": "Комментарий...",
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance and self.instance.pk:
            if self.instance.type:
                self.fields["category"].queryset = Category.objects.filter(type=self.instance.type)
            if self.instance.category:
                self.fields["subcategory"].queryset = SubCategory.objects.filter(
                    category=self.instance.category
                )
        else:
            self.fields["category"].queryset = Category.objects.none()
            self.fields["subcategory"].queryset = SubCategory.objects.none()
            self.fields["category"].widget.attrs["disabled"] = True
            self.fields["subcategory"].widget.attrs["disabled"] = True

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    #     self.fields["category"].queryset = Category.objects.none()
    #     self.fields["subcategory"].queryset = SubCategory.objects.none()

    #     if self.is_bound:
    #         type_id = self.data.get("type")
    #         if type_id:
    #             self.fields["category"].queryset = Category.objects.filter(type_id=type_id)

    #         category_id = self.data.get("category")
    #         if category_id:
    #             self.fields["subcategory"].queryset = SubCategory.objects.filter(
    #                 category_id=category_id
    #             )

    #     elif self.instance.pk:
    #         if self.instance.type:
    #             self.fields["category"].queryset = Category.objects.filter(
    #                 type=self.instance.type
    #             )

    #         if self.instance.category:
    #             self.fields["subcategory"].queryset = SubCategory.objects.filter(
    #                 category=self.instance.category
    #             )
    #     else:
    #         self.fields["category"].widget.attrs["disabled"] = True
    #         self.fields["subcategory"].widget.attrs["disabled"] = True

    def clean(self):
        cd = super().clean()

        type = cd.get("type")
        category = cd.get("category")
        subcategory = cd.get("subcategory")

        if type and category and category.type != type:
            self.add_error("category", "Категория не относится к выбранному типу")

        if category and subcategory and subcategory.category != category:
            self.add_error("subcategory", "Подкатегория не относится к выбранной категории")

        return cd
