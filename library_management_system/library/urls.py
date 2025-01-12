from django.urls import path
from . import views 

urlpatterns = [
    path("",views.home, name='home'),
    path('addbook/',views.addbook, name='addbook'),
    path('edit/<int:id>/', views.edit_book, name='edit_book'),
    path('delete/<int:id>/', views.delete, name='delete'),

]
