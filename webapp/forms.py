from django import forms
from .models import *

class MemberCreationForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = "__all__"


class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = "__all__"