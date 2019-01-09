from django import forms

from .models import Medicine
from .models import Request

class MedicineForm(forms.ModelForm):

    class Meta:
        model = Medicine
        fields = ('Название', 'Форма_выпуска', 'Способ_применения', 'Противопоказания', 'Выдача', 'Срок_годности', 'Наличие',)

class RequestForm(forms.ModelForm):

    class Meta:
        model = Request
        fields = ('Название', 'Форма_выпуска', 'Дозировка', 'Ваш_email_или_номер_телефона', )
