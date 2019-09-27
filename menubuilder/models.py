from django.db import models
from django.utils import timezone
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
from enum import Enum


class MenuType(Enum):
    LABEL = "Menu Label"
    OPTION = "Menu Option"
    ENTRY = "Entry Input"
    USSDCODE = "Dial Ussd Code"
    ROOT = "Root"
    USSDFLASH = "Ussd Flash Message"
    SMSTEXT = "SMS Text"


def types():
    return [(m_type.name, m_type.value) for m_type in MenuType]


class Menu(MPTTModel, models.Model):
    name = models.CharField(max_length=100)
    label_en = models.CharField(max_length=100)
    label_sw = models.CharField(max_length=100)
    order_num = models.IntegerField(default=0)
    menu_type = models.CharField(max_length=10, choices=types(), null=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='sub_menus')
    record_date = models.DateTimeField(default=timezone.now)
    sample_value = models.CharField(max_length=100, null=True, blank=True)

    class MPTTMeta:
        ordering = ['order_num', 'parent']

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('menu-create', kwargs={'parent_pk': self.parent_id})
