from django import forms
from .models import Menu


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['parent', 'menu_type', 'name', 'label_en', 'label_sw', 'order_num', 'sample_value']
        widgets = {
            'label_en': forms.Textarea(attrs={'rows': 3}),
            'label_sw': forms.Textarea(attrs={'rows': 3})
        }
