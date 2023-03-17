import datetime

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import DateInput, TimeInput

from dict_app.models import Login,Teacher


class LoginRegister(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label="password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="confirm password", widget=forms.PasswordInput)

    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2',)



class TeacherAddForm(forms.ModelForm):

    class Meta:
        model = Teacher
        fields = ('FirstName','LastName','Profile_picture','Email','Address','Phone','NumberRoom','Subjects')




class CsvForm(forms.modelform):
     class Meta:
         model = csv
         fields = ('file_name',)