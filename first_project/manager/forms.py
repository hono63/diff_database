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

class PersonPulldownForm(forms.Form):
    "PersonモデルのPulldown"
    Hist = forms.ModelChoiceField(label="Hist", widget=forms.Select(
        attrs={'onChange': 'form.submit();'}), queryset=Person.objects.all())

class ManagerPulldownForm(forms.Form):
    "ManagerモデルのPulldown"
    Hist = forms.ModelChoiceField(label="Hist", widget=forms.Select(
        attrs={'onChange': 'form.submit();'}), queryset=Manager.objects.all())

class WorkerPulldownForm(forms.Form):
    "WorkerモデルのPulldown"
    Hist = forms.ModelChoiceField(label="Hist", widget=forms.Select(
        attrs={'onChange': 'form.submit();'}), queryset=Worker.objects.all())


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