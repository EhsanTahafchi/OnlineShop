from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import get_user_model
from django.contrib.auth.admin import AdminUserCreationForm


class CustomUserCreationForm(AdminUserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username')
