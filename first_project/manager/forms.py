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

EMPTY_CHOICES = [('empty', '-----')]
NUMBER_CHOICES = [
    ('one', '1'),
    ('two', '2'),
    ('three', '3')
]


class PulldownForm(forms.Form):
    "Pulldownのサンプル"
    Hist = forms.ChoiceField(label="Hist", widget=forms.Select(
        attrs={'onChange': 'form.submit();'}), choices=EMPTY_CHOICES+NUMBER_CHOICES)
