from decimal import Decimal, InvalidOperation

from django.shortcuts import render

from .models import Category, Status, SubCategory, Transaction, Type

from django.http import JsonResponse

# view главной страницы
def transaction_list(request):
    # Сразу подгружаем необходимые поля
    transactions = Transaction.objects.select_related(
        "status", "type", "category", "subcategory"
    )

    # Получение полей
    status_id = request.GET.get("status")
    type_id = request.GET.get("type")
    category_id = request.GET.get("category")
    subcategory_id = request.GET.get("subcategory")
    min_amount = request.GET.get("min_amount")
    max_amount = request.GET.get("max_amount")
    comment = request.GET.get("comment", "").strip()
    date_from = request.GET.get("date_from")
    date_to = request.GET.get("date_to")

    # Фильтрация
    if status_id:
        transactions = transactions.filter(status_id=status_id)
    
    if type_id:
        transactions = transactions.filter(type_id=type_id)

    if category_id:
        transactions = transactions.filter(category_id=category_id)
    
    if subcategory_id:
        transactions = transactions.filter(subcategory_id=subcategory_id)
    
    if min_amount:
        try:
            transactions = transactions.filter(amount__gte=Decimal(min_amount))
        except InvalidOperation:
            pass
    
    if max_amount:
        try:
            transactions = transactions.filter(amount__lte=Decimal())
        except InvalidOperation:
            pass
    
    if comment:
        transactions = transactions.filter(comment__icontains=comment)
    
    if date_from:
        transactions = transactions.filter(created_at__gte=date_from)
    
    if date_to:
        transactions = transactions.filter(created_at__lte=date_to)

    # if status_id:
    #     transactions = transactions.filter(status_id=status_id)
    # if type_id:
    #     transactions = transactions.filter(type_id=type_id)
    # if category_id:
    #     transactions = transactions.filter(category_id=category_id)
    # if subcategory_id:
    #     transactions = transactions.filter(subcategory_id=subcategory_id)
    # if min_amount:
    #     try:
    #         transactions = transactions.filter(amount__gte=Decimal(min_amount))
    #     except InvalidOperation:
    #         pass
    # if max_amount:
    #     try:
    #         transactions = transactions.filter(amount__lte=Decimal(max_amount))
    #     except InvalidOperation:
    #         pass
    # if comment:
    #     transactions = transactions.filter(comment__icontains=comment)
    # if date_from:
    #     transactions = transactions.filter(created_at__gte=date_from)
    # if date_to:
    #     transactions = transactions.filter(created_at__lte=date_to)

    filters = {
        "date_from": date_from or "",
        "date_to": date_to or "",
        "status": status_id or "",
        "type": type_id or "",
        "category": category_id or "",
        "subcategory": subcategory_id or "",
        "min_amount": min_amount or "",
        "max_amount": max_amount or "",
        "comment": comment,
    }
    # if type_id:
    #     categories = Category.objects.filter(type_id=type_id)
    # if category_id:
    #     subcategories = SubCategory.objects.filter(category_id=category_id)

    context = {
        "transactions": transactions,
        "statuses": Status.objects.all(),
        "types": Type.objects.all(),
        "categories": Category.objects.filter(),
        "subcategories": SubCategory.objects.all(),
        "filters": filters,
        "has_filters": any(filters.values()),
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