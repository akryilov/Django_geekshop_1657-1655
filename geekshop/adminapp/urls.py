from django.urls import path

from adminapp.views import UserListView, IndexTemplateView, UserCreateView, UserUpdateView, UserDeleteView
from adminapp.views import CategoryListView
###
# import adminapp.views as adminapp
from adminapp.views import admin_products, admin_category_create, admin_category_update, admin_category_delete, admin_product_create, admin_product_delete, admin_product_update

app_name = 'adminapp'

urlpatterns = [

    path('', IndexTemplateView.as_view(), name='index'),
    path('users/', UserListView.as_view(), name = 'admin_users'),
    path('user-create/', UserCreateView.as_view(), name='admin_user_create'),
    path('user-update/<int:id>/', UserUpdateView.as_view(), name='admin_user_update'),
    path('user-delete/<int:id>/', UserDeleteView.as_view(), name='admin_user_delete'),


    path('categories/', CategoryListView.as_view(), name ='admin_categories'),
    path('category-create/', admin_category_create, name ='admin_category_create'),
    path('category-update/<int:id>/', admin_category_update, name ='admin_category_update'),
    path('category-delete/<int:id>/', admin_category_delete, name ='admin_category_delete'),


    path('products/', admin_products, name= 'admin_products'),
    path('product-create/', admin_product_create, name='admin_product_create'),
    path('product-update/<int:id>/', admin_product_update, name='admin_product_update'),
    path('product-delete/<int:id>/', admin_product_delete, name='admin_product_delete'),

]

