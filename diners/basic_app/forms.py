from django import forms
from django.core import validators
from basic_app.models import DinnersDate,Dinners

from django.contrib.auth.models import User
#from django.contrib.admin import widgets
from django.contrib.admin.widgets import AdminDateWidget
import datetime
import html5.forms.widgets as html5_widgets

class formAddDinner(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Dodaj obiadek'}))
"""
class formAddDinnerDate(forms.ModelForm):
    class Meta:
        model = DinnersDate
        fields = '__all__'
"""

class formDaysChoice(forms.Form):
    days = forms.MultipleChoiceField(choices=((1,"pon"),(2,"wto"),(3,"sro")),widget=forms.CheckboxSelectMultiple())

class formAddDinnerDate(forms.Form):

    def __init__(self, foo_choices,date_tab, *args, **kwargs):
        super(formAddDinnerDate, self).__init__(*args, **kwargs)
        #self.attrs={'id':'formfield'}
        self.fields['din'].choices = foo_choices
        self.fields['date'].choices = date_tab
    din = forms.ChoiceField(label="Obiad", widget=forms.Select(attrs={'class':'form-control','id':'dinn'}))
    date = forms.ChoiceField(label="Data",widget=forms.Select(attrs={'class':'form-control','id':'dat'}))

    def clean_din(self):
        din = self.cleaned_data['din']
        if din=='0':
            raise forms.ValidationError("Wybierz coś")
        return din
    def clean_date(self):
        date = self.cleaned_data['date']
        if date=='0':
            raise forms.ValidationError("Wybierz coś")
        return date

    #test = forms.DateField(widget=forms.DateInput(format='%Y-%m-%d'),initial=datetime.date.today())
    #test = forms.DateField(widget=forms.SelectDateWidget(),initial=datetime.date.today())
    #test2 = forms.DateField(widget=html5_widgets.DateInput())

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')
