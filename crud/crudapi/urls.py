from django.urls import path
from . import views


urlpatterns = [
    path('',views.ApiOverview,name = 'home'),
    path('create/',views.add_item,name = 'add-item'),
    path('all/',views.view_items,name = 'view-item'),
    path('update/<int:pk>/', views.update_items, name='update-items'),
    path('item/delete/<int:pk>/', views.delete_items, name='delete-items'),



]
