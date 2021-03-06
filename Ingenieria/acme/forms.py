from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from acme.models import ClientProfile, VendedorFijoProfile, VendedorAmbProfile, Product


class VendAmbForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(max_length=200, required=True)
    first_name = forms.CharField(max_length=200, required=True)
    last_name = forms.CharField(max_length=200, required=True)
    password1 = forms.CharField(widget=forms.PasswordInput)
    cash = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    debit = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    credit = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    student = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    avatar = forms.ImageField(required=False)
    check = forms.BooleanField(widget=forms.CheckboxInput(), required=False)


    class Meta:
        model = User
        fields = (
            'username', 'email', 'password1', 'password2', 'last_name', 'first_name', 'cash', 'debit', 'credit',
            'student', 'avatar', 'check')

    def save(self, commit=True):
        user = super(VendAmbForm, self).save(commit=True)
        password = self.clean_password()
        user.set_password(password)
        client = VendedorAmbProfile(user=user, cash=self.cleaned_data['cash'],
                                    debit=self.cleaned_data['debit'], credit=self.cleaned_data['credit'],
                                    student=self.cleaned_data['student'],
                                    avatar=self.cleaned_data['avatar'],
                                    check=self.cleaned_data['check'])
        if commit:
            client.save()
        return user

    def clean_password(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError("password must match")
        return password1

class VendFijoForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(max_length=200, required=True)
    first_name = forms.CharField(max_length=200, required=True)
    last_name = forms.CharField(max_length=200, required=True)
    password1 = forms.CharField(widget=forms.PasswordInput)
    init_time = forms.TimeField(required=True)
    end_time = forms.TimeField(required=True)
    cash = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    debit = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    credit = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    student = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    avatar = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = (
            'username', 'email', 'password1', 'password2', 'init_time', 'end_time', 'cash', 'debit', 'credit',
            'student',
            'first_name', 'last_name', 'avatar')

    def save(self, commit=True):
        user = super(VendFijoForm, self).save(commit=True)
        password = self.clean_password()
        user.set_password(password)
        client = VendedorFijoProfile(user=user, init_time=self.cleaned_data['init_time'],
                                     end_time=self.cleaned_data['end_time'], cash=self.cleaned_data['cash'],
                                     debit=self.cleaned_data['debit'], credit=self.cleaned_data['credit'],
                                     student=self.cleaned_data['student'],
                                     avatar=self.cleaned_data['avatar'])
        if commit:
            client.save()
        return user

    def clean_password(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError("password must match")
        return password1

class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(max_length=200, required=True)
    first_name = forms.CharField(max_length=200, required=True)
    last_name = forms.CharField(max_length=200, required=True)
    password1 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=True)
        password = self.clean_password()
        user.set_password(password)
        client = ClientProfile(user=user)
        if commit:
            client.save()
        return user

    def clean_password(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError("password must match")
        return password1

class ProductForm(forms.ModelForm):
    name = forms.CharField(required=True)
    cost = forms.IntegerField(required=True)
    stock = forms.IntegerField(required=True)
    description = forms.CharField(max_length=300, required=False)
    category = forms.CharField(max_length=200, required=True)
    photo = forms.ImageField(required=True)

    class Meta:
        model = Product
        exclude = ('user',)
        fields = ('cost', 'name', 'description', 'stock', 'category', 'photo', 'user')

    def save(self, commit=True):
        prod = Product(cost=self.cleaned_data['cost'],
                       name=self.cleaned_data['name'],
                       stock=self.cleaned_data['stock'],
                       description=self.cleaned_data['description'],
                       category=self.cleaned_data['category'],
                       photo=self.cleaned_data['photo'])
        prod.save()
        return prod

class UpdateProfile(forms.ModelForm):
    username = forms.CharField(required=False)
    email = forms.EmailField(required=False)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

    def clean_email(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')

        if email and User.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError(
                'This email address is already in use. Please supply a different email address.')
        return email

    def save(self, user, commit=True):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()

        return user


