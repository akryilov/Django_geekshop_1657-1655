from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from authapp.models import User

####
from mainapp.models import Product, ProductCategories


class UserAdminRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'last_name', 'first_name', 'email', 'image', 'age')

    def __init__(self, *args, **kwargs):
        super(UserAdminRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Введите имя пользователя'
        self.fields['password1'].widget.attrs['placeholder'] = 'Введите пароль'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Введите фамилию'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Введите имя'
        self.fields['email'].widget.attrs['placeholder'] = 'Введите email'
        self.fields['password2'].widget.attrs['placeholder'] = 'Подтвердите пароль'
        self.fields['image'].widget.attrs['placeholder'] = 'Добавить фотографию'
        self.fields['age'].widget.attrs['placeholder'] = 'Возраст'

        for filed_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
            self.fields['image'].widget.attrs['class'] = 'custom-file-input'


class UserAdminProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'last_name', 'first_name', 'email', 'image', 'age')

    def __init__(self, *args, **kwargs):
        super(UserAdminProfileForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['readonly'] = True
        self.fields['email'].widget.attrs['readonly'] = True

        for filed_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
        self.fields['image'].widget.attrs['class'] = 'custom-file-input'

#####

class ProductAdminRegisterForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Введите имя продукта'
        self.fields['descriptions'].widget.attrs['placeholder'] = 'Описание продукта'
        self.fields['price'].widget.attrs['placeholder'] = 'Введите стоимость продукта'
        self.fields['quantity'].widget.attrs['placeholder'] = 'Введите количество'
        self.fields['category'].widget.attrs['placeholder'] = 'Выберите категорию'

        for filed_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
            self.fields['image'].widget.attrs['class'] = 'custom-file-input'


class ProductAdminProfileForm(UserChangeForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ProductAdminProfileForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['readonly'] = True

        for filed_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'

        self.fields['image'].widget.attrs['class'] = 'custom-file-input'


#####

class CategoryAdminRegisterForm(forms.ModelForm):
    class Meta:
        model = ProductCategories
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Введите имя категории'
        self.fields['descriptions'].widget.attrs['placeholder'] = 'Описание категории'

        for filed_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'


class CategoryAdminProfileForm(UserChangeForm):
    class Meta:
        model = ProductCategories
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CategoryAdminProfileForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['readonly'] = False

        for filed_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
