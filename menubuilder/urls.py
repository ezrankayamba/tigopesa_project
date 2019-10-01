from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.MenuListView.as_view(), name="menubuilder"),
    path('<parent_pk>/create/', views.MenuCreateView.as_view(), name="menu-create"),
    path('detail/<pk>', views.MenuDetailView.as_view(), name="menu-detail"),
    path('update/<pk>', views.MenuUpdateView.as_view(), name="menu-update"),
    path('navupdate/', views.MenuNavUpdateView.as_view(), name="menu-nav-update"),
    path('navupdate/<pk>', views.MenuNavUpdateView.as_view(), name="menu-nav-update"),
]
