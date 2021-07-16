from django.urls import path
from .views import (category_list, category_create, category_edit, category_delete,
                    product_list, product_create, product_edit, product_delete, home_page2, login_page, logout_page)

urlpatterns = [
    path('', home_page2, name="home_page2"),
    path('login/', login_page, name="login_page"),
    path('logout/', logout_page, name="logout"),


    path('category/', category_list, name="category_list"),
    path('category/create', category_create, name="category_create"),
    path('category/<int:pk>/edit', category_edit, name="category_edit"),
    path('category/<int:pk>/delete', category_delete, name="category_delete"),

    path('product/', product_list, name="product_list"),
    path('product/create', product_create, name="product_create"),
    path('product/<int:pk>/edit', product_edit, name="product_edit"),
    path('product/<int:pk>/delete', product_delete, name="product_delete"),
]