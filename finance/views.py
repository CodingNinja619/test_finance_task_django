from decimal import Decimal, InvalidOperation

from django.shortcuts import get_object_or_404, redirect, render

from .models import Category, Status, SubCategory, Transaction, Type

from django.http import JsonResponse

from .forms import TransactionFilterForm, TransactionForm, TypeForm, StatusForm, CategoryForm, SubCategoryForm

# view главной страницы
def transaction_list(request):
   
    form = TransactionFilterForm(request.GET or None)

    # Сразу подгружаем необходимые поля
    qs = Transaction.objects.select_related(
        "status", "type", "category", "subcategory"
    )
    # Фильтрация
    if form.is_valid():
        cd = form.cleaned_data

        if cd["date_from"]:
            qs = qs.filter(created_at__gte=cd["date_from"])
        if cd["date_to"]:
            qs = qs.filter(created_at__lte=cd["date_to"])

        if cd["status"]:
            qs = qs.filter(status=cd["status"])

        if cd["type"]:
            qs = qs.filter(type=cd["type"])

        if cd["category"]:
            qs = qs.filter(category=cd["category"])

        if cd["subcategory"]:
            qs = qs.filter(subcategory=cd["subcategory"])

        if cd["min_amount"]:
            qs = qs.filter(amount__gte=cd["min_amount"])

        if cd["max_amount"]:
            qs = qs.filter(amount__lte=cd["max_amount"])

        if cd["comment"]:
            qs = qs.filter(comment__icontains=cd["comment"])


    context = {
        "transactions": qs,
        "form": form,

    }
    return render(request, "finance/transaction_list.html", context)

# Получение категорий (через AJAX)
def get_categories(request):
    type_id = request.GET.get("type_id")
    if not type_id or type_id == "all":
        categories = Category.objects.all()
    else:
        categories = Category.objects.filter(type_id=type_id)

    data = list(categories.values("id", "name", "type_id"))

    return JsonResponse(data, safe=False)

# Получение подкатегорий (через AJAX)
def get_subcategories(request):
    category_id = request.GET.get("category_id")
    subcategories = SubCategory.objects.filter(category_id=category_id)

    data = list(subcategories.values("id", "name", "category_id"))

    return JsonResponse(data, safe=False)

# Создание, изменение, удаление транзакций
def transaction_create(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("finance:transaction_list")
    else:
        form = TransactionForm()

    return render(request, "finance/transaction.html", {"form": form})


def transaction_edit(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)

    if request.method == "POST":
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect("finance:transaction_list")
    else:
        form = TransactionForm(instance=transaction)

    return render(request, "finance/transaction.html", {"form": form})

def transaction_delete(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == "POST":
        transaction.delete()
    
    return redirect("finance:transaction_list")

# Страница справочников
def directories(request):
    statuses = Status.objects.all()
    types = Type.objects.all()

    status_form = StatusForm()
    type_form = TypeForm()
    category_form = CategoryForm()
    subcategory_form = SubCategoryForm()

    return render(request, "finance/directories.html", {
        "statuses": statuses,
        "types": types,
        "status_form": status_form,
        "type_form": type_form,
        "category_form": category_form,
        "subcategory_form": subcategory_form,
    })

# CRUD для справочников
def type_create(request):
    if request.method == "POST":
        form = TypeForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect("finance:directories")

def status_create(request):
    if request.method == "POST":
        form = StatusForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect("finance:directories")

def category_create(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect("finance:directories")

def subcategory_create(request):
    if request.method == "POST":
        form = SubCategoryForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect("finance:directories")

def status_edit(request, pk):
    status = get_object_or_404(Status, pk=pk)

    if request.method == "POST":
        form = StatusForm(request.POST, instance=status)
        if form.is_valid():
            form.save()

    return redirect("finance:directories")

def type_edit(request, pk):
    type_obj = get_object_or_404(Type, pk=pk)

    if request.method == "POST":
        form = TypeForm(request.POST, instance=type_obj)
        if form.is_valid():
            form.save()

    return redirect("finance:directories")

def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()

    return redirect("finance:directories")

def subcategory_edit(request, pk):
    subcategory = get_object_or_404(SubCategory, pk=pk)

    if request.method == "POST":
        form = SubCategoryForm(request.POST, instance=subcategory)
        if form.is_valid():
            form.save()

    return redirect("finance:directories")

def type_delete(request, pk):
    type_obj = get_object_or_404(Type, pk=pk)

    if request.method == "POST":
        type_obj.delete()

    return redirect("finance:directories")


def status_delete(request, pk):
    status = get_object_or_404(Status, pk=pk)

    if request.method == "POST":
        status.delete()

    return redirect("finance:directories")


def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.method == "POST":
        category.delete()

    return redirect("finance:directories")


def subcategory_delete(request, pk):
    subcategory = get_object_or_404(SubCategory, pk=pk)

    if request.method == "POST":
        subcategory.delete()

    return redirect("finance:directories")