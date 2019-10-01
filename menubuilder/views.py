from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from .models import Menu
from django import forms
from .forms import MenuForm
from django.db.models import Q, Count


def home(request):
    context = {}
    return render(request, 'menubuilder/home.html', context)


class MenuListView(ListView):
    model = Menu
    template_name = 'menubuilder/home.html'
    context_object_name = 'menus'
    ordering = ['order_num']

    def get_queryset(self):
        return Menu.objects.all()


class MenuDetailView(DetailView):
    model = Menu
    template_name = 'menubuilder/menu_detail.html'

    def get_object(self):
        print(self.kwargs)
        # print(args)
        if 'pk' in self.kwargs:
            return Menu.objects.get(pk=self.kwargs.get('pk'))
        return Menu.objects.get(parent__isnull=True)


class MenuUpdateView(UpdateView):
    model = Menu
    form_class = MenuForm

    def form_valid(self, form):
        return super().form_valid(form)


class MenuNavUpdateView(UpdateView):
    model = Menu
    fields = ['parent', 'menu_type', 'name', 'label_en', 'label_sw', 'order_num', 'sample_value']
    template_name = 'menubuilder/menu_nav_form.html'

    def get_object(self):
        if 'pk' in self.request.GET:
            return Menu.objects.get(pk=self.request.GET.get('pk'))
        return Menu.objects.get(parent__isnull=True)


class MenuCreateView(CreateView):
    model = Menu
    form_class = MenuForm

    def get_initial(self, *args, **kwargs):
        initial = super(MenuCreateView, self).get_initial(**kwargs)
        initial['parent'] = self.kwargs.get('parent_pk')
        return initial

    def get_context_data(self, **kwargs):
        parent_pk = self.kwargs.get('parent_pk')
        kwargs['parent'] = Menu.objects.filter(pk=parent_pk).first()
        return super(MenuCreateView, self).get_context_data(**kwargs)

    def form_valid(self, form):
        return super().form_valid(form)
