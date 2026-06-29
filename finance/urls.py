from django.urls import path

from . import views

app_name = "finance"

urlpatterns = [
    path("", views.transaction_list, name="transaction_list"),
    path("transactions/create", views.transaction_create, name="transaction_create"),
    path("transactions/<int:pk>/edit", views.transaction_update, name="transaction_update"),


    path("ajax/categories/", views.get_categories, name="ajax_categories"),
    path("ajax/subcategories/", views.get_subcategories, name="ajax_subcategories"),
]
