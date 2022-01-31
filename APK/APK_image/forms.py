from django.forms import ModelForm
from django import forms
from APK_image.models import Violation


class ViolationForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ViolationForm, self).__init__(*args, **kwargs)
        self.fields['gas_pipeline'].empty_label = 'Категория не выбрана'

    class Meta:
        model = Violation
        fields = ['object', 'gas_pipeline', 'text_violation', 'date_elimination', 'photo_violation']
        widgets = {'object': forms.TextInput(attrs={'class': 'form-control'}),
                   'gas_pipeline': forms.Select(attrs={'class': 'custom-select'}),
                   'text_violation': forms.Textarea(attrs={'class': 'form-control'}),
                   'date_elimination': forms.SelectDateWidget(attrs={'class': 'input-append date'})
                   }
