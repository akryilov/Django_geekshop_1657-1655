from django.http import HttpResponseRedirect
# from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm, ProductAdminRegisterForm, \
    ProductAdminProfileForm, CategoryAdminProfileForm, CategoryAdminRegisterForm
from authapp.models import User
from django.contrib.auth.decorators import user_passes_test

###
from mainapp.models import Product, ProductCategories
from django.shortcuts import get_object_or_404, render


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'adminapp/admin.html')


@user_passes_test(lambda u: u.is_superuser)
def admin_users(request):
    context = {
        'title': 'Админка | Пользователи',
        'users': User.objects.all()
    }
    return render(request, 'adminapp/admin-users-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_user_create(request):
    if request.method == 'POST':
        form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:admin_users'))
        else:
            print(form.errors)
    else:
        form = UserAdminRegisterForm()
    context = {
        'title': 'Админка | Регистрация',
        'form': form
    }

    return render(request, 'adminapp/admin-users-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_user_update(request, id):
    user_select = User.objects.get(id=id)
    if request.method == 'POST':
        form = UserAdminProfileForm(data=request.POST, instance=user_select, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:admin_users'))
    else:
        form = UserAdminProfileForm(instance=user_select)
    context = {
        'title': 'Админка | Обновление пользователя',
        'form': form,
        'user_select': user_select
    }
    return render(request, 'adminapp/admin-users-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_user_delete(request, id):
    user = User.objects.get(id=id)
    user.is_active = False
    user.save()
    return HttpResponseRedirect(reverse('adminapp:admin_users'))


@user_passes_test(lambda u: u.is_superuser)
def admin_categories(request):
    context = {
        'title': 'Админка | Категории',
        'categories': ProductCategories.objects.all()
    }
    return render(request, 'adminapp/admin-categories-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_category_create(request):
    if request.method == 'POST':
        form = CategoryAdminRegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:admin_products'))
        else:
            print(form.errors)
    else:
        form = CategoryAdminRegisterForm()
    context = {
        'title': 'Админка | Категории',
        'form': form
    }

    return render(request, 'adminapp/admin-categories-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_category_update(request, id):
    category_select = ProductCategories.objects.get(id=id)
    if request.method == 'POST':
        form = CategoryAdminProfileForm(data=request.POST, instance=category_select, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:admin_categories'))
    else:
        form = CategoryAdminProfileForm(instance=category_select)
    context = {
        'title': 'Админка | Обновление категории',
        'form': form,
        'category_select': category_select
    }
    return render(request, 'adminapp/admin-categories-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_category_delete(request, id):
    category = ProductCategories.objects.get(id=id)
    category.is_active = False
    category.save()
    return HttpResponseRedirect(reverse('adminapp:admin_categories'))


@user_passes_test(lambda u: u.is_superuser)
def admin_products(request):
    context = {
        'title': 'Админка | Продукты',
        'products': Product.objects.all()
        }
    return render(request, 'adminapp/admin-products-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_product_create(request):
    if request.method == 'POST':
        form = ProductAdminRegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:admin_products'))
        else:
            print(form.errors)
    else:
        form = ProductAdminRegisterForm()
    context = {
        'title': 'Админка | Продукты',
        'form': form
    }

    return render(request, 'adminapp/admin-products-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_product_update(request, id):
    product_select = Product.objects.get(id=id)
    if request.method == 'POST':
        form = ProductAdminProfileForm(data=request.POST, instance=product_select, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:admin_products'))
    else:
        form = ProductAdminProfileForm(instance=product_select)
    context = {
        'title': 'Админка | Обновление продукта',
        'form': form,
        'product_select': product_select
    }
    return render(request, 'adminapp/admin-products-update-delete.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admin_product_delete(request, id):
    product = Product.objects.get(id=id)
    product.is_active = False
    product.save()
    return HttpResponseRedirect(reverse('adminapp:admin_products'))
