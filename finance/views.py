from decimal import Decimal, InvalidOperation

from django.shortcuts import get_object_or_404, redirect, render

from .models import Category, Status, SubCategory, Transaction, Type

from django.http import JsonResponse

from .forms import TransactionFilterForm, TransactionForm

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

def get_categories(request):
    type_id = request.GET.get("type_id")
    if not type_id or type_id == "all":
        categories = Category.objects.all()
    else:
        categories = Category.objects.filter(type_id=type_id)

    data = list(categories.values("id", "name"))

    return JsonResponse(data, safe=False)

def get_subcategories(request):
    category_id = request.GET.get("category_id")
    subcategories = SubCategory.objects.filter(category_id=category_id)

    data = list(subcategories.values("id", "name"))

    return JsonResponse(data, safe=False)

def transaction_create(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("finance:transaction_list")
    else:
        form = TransactionForm()

    return render(request, "finance/transaction.html", {"form": form})


def transaction_update(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)

    if request.method == "POST":
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect("finance:transaction_list")
    else:
        form = TransactionForm(instance=transaction)

    return render(request, "finance/transaction.html", {"form": form})
