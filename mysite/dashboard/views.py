from django.shortcuts import render, redirect
from .forms import CategoryForm, ProductForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from food.models import Category, Product


def login_required_decorator(func):
    return login_required(func, login_url="login_page")


@login_required_decorator
def home_page2(request):
    return render(request, "dashboard/index.html")


def login_page(request):
    if request.POST:
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home_page2")
    return render(request, "dashboard/login.html")


@login_required_decorator
def logout_page(request):
    logout(request)
    return redirect("login_page")


@login_required_decorator
def category_list(request):
    category = Category.objects.all()
    ctx = {
        "categories": category
    }
    return render(request, "category/list.html", ctx)


def category_create(request):
    model = Category()
    form = CategoryForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect("category_list")
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, "category/form.html", ctx)


def category_edit(request, pk):
    model = Category.objects.get(pk=pk)
    form = CategoryForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect("category_list")
    ctx = {
        "form": form,
        "model": model
    }
    return render(request, "category/form.html", ctx)


def category_delete(request, pk):
    model = Category.objects.get(pk=pk)
    model.delete()
    return redirect("category_list")


@login_required_decorator
def product_list(request):
    product = Product.objects.all()
    ctx = {
        "products": product
    }
    return render(request, "product/list.html", ctx)


def product_create(request):
    model = Product()
    form = ProductForm(request.POST or None, request.FILES or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect("product_list")
        else:
            print(form.errors)
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, "product/form.html", ctx)


def product_edit(request, pk):
    model = Product.objects.get(pk=pk)
    form = ProductForm(request.POST or None, request.FILES or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect("product_list")
    ctx = {
        "form": form,
        "model": model
    }
    return render(request, "product/form.html", ctx)


def product_delete(request, pk):
    model = Product.objects.get(pk=pk)
    model.delete()
    return redirect("product_list")
