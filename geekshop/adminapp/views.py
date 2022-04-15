from django.http import HttpResponseRedirect
# from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm
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


def admin_categories(request):
    categories_list = ProductCategories.objects.all()
    context = {
        'title': 'Админка | Категории',
        'objects': categories_list
    }
    return render(request, 'adminapp/categories.html', context)


def admin_category_create(request):
    pass


def admin_category_update(request, id):
    pass


def admin_category_delete(request, id):
    pass


def admin_products(request):
    title = 'Админка | Продукты'
    products_list = Product.objects.all()
    context = {
        'title': title,
        'objects': products_list,
    }
    return render(request, 'adminapp/admin-products-read.html', context)


def admin_product_create(request, id):
    pass


def admin_product_read(request, id):
    pass


def admin_product_update(request, id):
    pass


def admin_product_delete(request, id):
    pass
