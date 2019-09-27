from django.urls import path, include
from . import views


urlpatterns = [
    # path('', views.home, name="menubuilder"),
    path('', views.MenuListView.as_view(), name="menubuilder"),
    path('<parent_pk>/create/', views.MenuCreateView.as_view(), name="menu-create"),
    path('detail/<pk>', views.MenuDetailView.as_view(), name="menu-detail"),
    path('update/<pk>', views.MenuUpdateView.as_view(), name="menu-update"),
]
