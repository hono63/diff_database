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

class PulldownForm(forms.Form):
    "汎用Pulldownフォーム"
    Hist = forms.ModelChoiceField(label="Hist", widget=forms.Select(
        attrs={'onChange': 'form.submit();'}), queryset=None)
    def __init__(self, model, *args, **kwargs):
        super(PulldownForm, self).__init__(*args,**kwargs) # これを呼ばないとfieldsが生成されない 
        self.queryset = model.objects.all()
        self.fields['Hist'].queryset = model.objects.all()


EMPTY_CHOICES = [('empty', '-----')]
NUMBER_CHOICES = [
    ('one', '1'),
    ('two', '2'),
    ('three', '3')
]

class PulldownFormSample(forms.Form):
    "Pulldownのサンプル"
    Hist = forms.ChoiceField(label="Hist", widget=forms.Select(
        attrs={'onChange': 'form.submit();'}), choices=EMPTY_CHOICES+NUMBER_CHOICES)