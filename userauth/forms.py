from .models import CustomUser
from wagtail.users.forms import UserCreationForm, UserEditForm
from django.forms import DateInput

class WagtailUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        widgets = {'birthdate': DateInput(attrs={'type':'date'})}


class WagtailUserEditForm(UserEditForm):
    class Meta(UserEditForm.Meta):
        model = CustomUser
        widgets = {'birthdate': DateInput(attrs={'type':'date'})}