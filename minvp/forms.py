# Imports from Django
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# Imports from this module (explicit relative imports)
from .models import Member


class MemberCreationForm(UserCreationForm):
    """
    A form that creates a user, with no privileges, from the given email and
    password.
    """

    def __init__(self, *args, **kargs):
        super(MemberCreationForm, self).__init__(*args, **kargs)
        del self.fields['username']

    class Meta:
        model = Member
        fields = ("email",)

class MemberChangeForm(UserChangeForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    def __init__(self, *args, **kargs):
        super(MemberChangeForm, self).__init__(*args, **kargs)
        del self.fields['username']

    class Meta:
        model = Member