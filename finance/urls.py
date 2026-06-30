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

    path('directories/type/create/', views.type_create, name='type_create'),
    path('directories/type/<int:pk>/edit/', views.type_edit, name='type_edit'),
    path('directories/type/<int:pk>/delete/', views.type_delete, name='type_delete'),

    path("directories/status/create/", views.status_create, name="status_create"),
    path("directories/status/<int:pk>/edit/", views.status_edit, name="status_edit"),
    path("directories/status/<int:pk>/delete/", views.status_delete, name="status_delete"),

    path("directories/category/create/", views.category_create, name="category_create"),
    path("directories/category/<int:pk>/edit/", views.category_edit, name="category_create"),
    path("directories/category/<int:pk>/delete/", views.category_delete, name="category_delete"),
    

    path("directories/subcategory/create/", views.subcategory_create, name="subcategory_create"),
    path("directories/subcategory/<int:pk>/edit/", views.subcategory_edit, name="subcategory_edit"),
    path("directories/subcategory/<int:pk>/delete/", views.subcategory_delete, name="subcategory_delete"),

]
