from django import forms
from .models import *


class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['placeholder'] = visible.field.label

    class Meta:
        model = Product
        fields = [
            "name", "price", "product_code", "age_start", "age_end", "height",
            "width", "length", "weight", "concrete", "installation_time", "params",
            "photo"
        ]


class TagForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['placeholder'] = visible.field.label

    class Meta:
        model = Tag
        fields = ["name"]


class CategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['placeholder'] = visible.field.label

    class Meta:
        model = Category
        fields = ["name"]


class LoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['placeholder'] = visible.field.label

    login = forms.CharField(max_length=255, label='Логин')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')


class RegForm(forms.ModelForm):
    username = forms.CharField(max_length=255, label='Логин')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Пароль (повторно)')
    email = forms.EmailField(label='email')
    phone_number = forms.CharField(max_length=32, label='Номер телефона')
    name = forms.CharField(max_length=255, label='Имя')
    surname = forms.CharField(max_length=255, label='Фамилия')

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'password2', 'phone_number', 'name', 'surname']


class RoleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['placeholder'] = visible.field.label

    class Meta:
        model = Role
        fields = [
            "name", "access_to_admin_panel"
        ]


class OrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['placeholder'] = visible.field.label

    class Meta:
        model = Order
        fields = [
            'contacts', 'status'
        ]


class OrderContactsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['placeholder'] = visible.field.label

    class Meta:
        model = Order
        fields = [
            'contacts'
        ]


class UserRedForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['placeholder'] = visible.field.label

    class Meta:
        model = CustomUser
        fields = [
            'username', 'phone_number', 'email', 'name', 'surname'
        ]


class ReadyProjectForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['placeholder'] = visible.field.label

    class Meta:
        model = Ready_project
        fields = [
            "name", "product_code", "price", "description", "video"
        ]

class CalcProjectForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['placeholder'] = visible.field.label

    class Meta:
        model = Calculated_project
        fields = [
            "name", "product_code", "price", "description", "file"
        ]
