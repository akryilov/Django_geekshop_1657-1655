from django.http import HttpResponseRedirect
# from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy

from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm, ProductAdminRegisterForm, \
    ProductAdminProfileForm, CategoryAdminProfileForm, CategoryAdminRegisterForm
from authapp.models import User
from django.contrib.auth.decorators import user_passes_test

from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DeleteView

###
from adminapp.mixin import BaseClassContextMixin, CustomDispatchMixin, UserDispatchMixin
from mainapp.models import Product, ProductCategories
from django.shortcuts import render


# @user_passes_test(lambda u: u.is_superuser)
# def index(request):
#     return render(request, 'adminapp/admin.html')


class IndexTemplateView(TemplateView, BaseClassContextMixin, CustomDispatchMixin):
    template_name = 'adminapp/admin.html'
    title = 'Главная страница'

    # @method_decorator(user_passes_test(lambda u: u.is_superuser))
    # def dispatch(self, request, *args, **kwargs):
    #     return super(IndexTemplateView, self).dispatch(request, *args, **kwargs)

    # def get_context_data(self, **kwargs):
    #     context = super(IndexTemplateView, self).get_context_data(**kwargs)
    #     context['title'] = 'Главная страница'
    #     return context


class UserListView(ListView, BaseClassContextMixin, CustomDispatchMixin, UserDispatchMixin):
    model = User
    template_name = 'adminapp/admin-users-read.html'
    title = 'Админка | Пользователи'
    context_object_name = 'users'


# @user_passes_test(lambda u: u.is_superuser)
# def admin_users(request):
#     context = {
#         'title': 'Админка | Пользователи',
#         'users': User.objects.all()
#     }
#     return render(request, 'adminapp/admin-users-read.html', context)


class UserCreateView(CreateView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = 'adminapp/admin-users-create.html'
    form_class = UserAdminRegisterForm
    title = 'Админка | Регистрация'
    success_url = reverse_lazy('adminapp:admin_users')


# @user_passes_test(lambda u: u.is_superuser)
# def admin_user_create(request):
#
#     if request.method == 'POST':
#         form = UserAdminRegisterForm(data=request.POST,files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('adminapp:admin_users'))
#         else:
#             print(form.errors)
#     else:
#         form = UserAdminRegisterForm()
#     context = {
#         'title': 'Админка | Регистрация',
#         'form':form
#     }
#
#     return render(request,'adminapp/admin-users-create.html',context)


class UserUpdateView(UpdateView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    title = 'Админка | Обновление пользователя'
    success_url = reverse_lazy('adminapp:admin_users')


# @user_passes_test(lambda u: u.is_superuser)
# def admin_user_update(request,id):
#     user_select = User.objects.get(id=id)
#     if request.method == 'POST':
#         form = UserAdminProfileForm(data=request.POST,instance=user_select,files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('adminapp:admin_users'))
#     else:
#         form = UserAdminProfileForm(instance=user_select)
#     context = {
#          'title': 'Админка | Обновление пользователя',
#          'form':form,
#          'user_select':user_select
#     }
#     return render(request, 'adminapp/admin-users-update-delete.html', context)


class UserDeleteView(DeleteView, CustomDispatchMixin):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('adminapp:admin_users')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


# @user_passes_test(lambda u: u.is_superuser)
# def admin_user_delete(request,id):
#     user = User.objects.get(id=id)
#     user.is_active = False
#     user.save()
#     return HttpResponseRedirect(reverse('adminapp:admin_users'))


class CategoryListView(ListView, BaseClassContextMixin, CustomDispatchMixin):
    model = ProductCategories
    template_name = 'adminapp/admin-categories-read.html'
    title = 'Админка | Категории'
    context_object_name = 'categories'


# @user_passes_test(lambda u: u.is_superuser)
# def admin_categories(request):
#     context = {
#         'title': 'Админка | Категории',
#         'categories': ProductCategories.objects.all()
#     }
#     return render(request, 'adminapp/admin-categories-read.html', context)


class CategoryCreateView(CreateView, BaseClassContextMixin, CustomDispatchMixin):
    model = ProductCategories
    template_name = 'adminapp/admin-categories-create.html'
    form_class = CategoryAdminRegisterForm
    title = 'Админка | Категории'
    success_url = reverse_lazy('adminapp:admin_categories')


# @user_passes_test(lambda u: u.is_superuser)
# def admin_category_create(request):
#     if request.method == 'POST':
#         form = CategoryAdminRegisterForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('adminapp:admin_products'))
#         else:
#             print(form.errors)
#     else:
#         form = CategoryAdminRegisterForm()
#     context = {
#         'title': 'Админка | Категории',
#         'form': form
#     }
#
#     return render(request, 'adminapp/admin-categories-create.html', context)


class CategoryUpdateView(UpdateView, BaseClassContextMixin, CustomDispatchMixin):
    model = ProductCategories
    template_name = 'adminapp/admin-categories-update-delete.html'
    form_class = CategoryAdminProfileForm
    title = 'Админка | Категории'
    success_url = reverse_lazy('adminapp:admin_categories')


# @user_passes_test(lambda u: u.is_superuser)
# def admin_category_update(request, id):
#     category_select = ProductCategories.objects.get(id=id)
#     if request.method == 'POST':
#         form = CategoryAdminProfileForm(data=request.POST, instance=category_select, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('adminapp:admin_categories'))
#     else:
#         form = CategoryAdminProfileForm(instance=category_select)
#     context = {
#         'title': 'Админка | Обновление категории',
#         'form': form,
#         'category_select': category_select
#     }
#     return render(request, 'adminapp/admin-categories-update-delete.html', context)


class CategoryDeleteView(DeleteView, CustomDispatchMixin):
    model = ProductCategories
    template_name = 'adminapp/admin-categories-update-delete.html'
    form_class = CategoryAdminProfileForm
    success_url = reverse_lazy('adminapp:admin_categories')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


#
# @user_passes_test(lambda u: u.is_superuser)
# def admin_category_delete(request, id):
#     category = ProductCategories.objects.get(id=id)
#     category.is_active = False
#     category.save()
#     return HttpResponseRedirect(reverse('adminapp:admin_categories'))


class ProductListView(ListView, BaseClassContextMixin, CustomDispatchMixin):
    model = Product
    template_name = 'adminapp/admin-products-read.html'
    title = 'Админка | Продукты'
    context_object_name = 'products'


#
# @user_passes_test(lambda u: u.is_superuser)
# def admin_products(request):
#     context = {
#         'title': 'Админка | Продукты',
#         'products': Product.objects.all()
#     }
#     return render(request, 'adminapp/admin-products-read.html', context)


class ProductCreateView(CreateView, BaseClassContextMixin, CustomDispatchMixin):
    model = Product
    template_name = 'adminapp/admin-products-create.html'
    form_class = ProductAdminRegisterForm
    title = 'Админка | Продукты'
    success_url = reverse_lazy('adminapp:admin_products')


# @user_passes_test(lambda u: u.is_superuser)
# def admin_product_create(request):
#     if request.method == 'POST':
#         form = ProductAdminRegisterForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('adminapp:admin_products'))
#         else:
#             print(form.errors)
#     else:
#         form = ProductAdminRegisterForm()
#     context = {
#         'title': 'Админка | Продукты',
#         'form': form
#     }
#
#     return render(request, 'adminapp/admin-products-create.html', context)


class ProductUpdateView(UpdateView, BaseClassContextMixin, CustomDispatchMixin):
    model = Product
    template_name = 'adminapp/admin-products-update-delete.html'
    form_class = ProductAdminProfileForm
    title = 'Админка | Обновление продукта'
    success_url = reverse_lazy('adminapp:admin_products')

# @user_passes_test(lambda u: u.is_superuser)
# def admin_product_update(request, id):
#     product_select = Product.objects.get(id=id)
#     if request.method == 'POST':
#         form = ProductAdminProfileForm(data=request.POST, instance=product_select, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('adminapp:admin_products'))
#     else:
#         form = ProductAdminProfileForm(instance=product_select)
#     context = {
#         'title': 'Админка | Обновление продукта',
#         'form': form,
#         'product_select': product_select
#     }
#     return render(request, 'adminapp/admin-products-update-delete.html', context)



class ProductDeleteView(DeleteView, CustomDispatchMixin):
    model = Product
    template_name = 'adminapp/admin-products-update-delete.html'
    form_class = ProductAdminProfileForm
    success_url = reverse_lazy('adminapp:admin_products')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

#
# @user_passes_test(lambda u: u.is_superuser)
# def admin_product_delete(request, id):
#     product = Product.objects.get(id=id)
#     product.is_active = False
#     product.save()
#     return HttpResponseRedirect(reverse('adminapp:admin_products'))
