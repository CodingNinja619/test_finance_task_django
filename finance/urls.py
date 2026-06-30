from django.urls import path

from . import views

app_name = "finance"

urlpatterns = [
    path("", views.transaction_list, name="transaction_list"),

    path("ajax/categories/", views.get_categories, name="ajax_categories"),
    path("ajax/subcategories/", views.get_subcategories, name="ajax_subcategories"),

    path("transactions/create", views.transaction_create, name="transaction_create"),
    path("transactions/edit/<int:pk>", views.transaction_edit, name="transaction_edit"),
    path("transactions/delete/<int:pk>", views.transaction_delete, name="transaction_delete"),

    path("directories/", views.directories, name="directories"),
]
