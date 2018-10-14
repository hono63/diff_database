from django.forms import ModelForm
from manager.models import Person, Worker, Manager


class PersonForm(ModelForm):
    """Personのメタ(?)フォーム"""
    class Meta:
        model = Person
        fields = ('name', 'sex', )

class ManagerForm(ModelForm):
    """Managerフォーム"""
    class Meta:
        model = Manager
        fields = ('person', 'department', )

class WorkerForm(ModelForm):
    """Workerのフォーム"""
    class Meta:
        model = Worker
        fields = ('manager', 'person', )


from django import forms

EMPTY_CHOICES = (('', '-'*10))
NUMBER_CHOICES = (
    ('one', '1'),
    ('two', '2'),
    ('three', '3')
    )

class PulldownForm(forms.Form):
    "Pulldownのサンプル"
    number_choice = forms.ChoiceField(label="番号", widget=forms.Select, choices=NUMBER_CHOICES)