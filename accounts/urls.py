from django.urls import path
from .views import deleteUser, editCompany, editEmployee, loginPage, logoutUser, register


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('editcompany/', editCompany, name='editcompany'),
    path('editemployee/', editEmployee, name='editemployee'),
    path('deleteuser/<str:pk>', deleteUser, name='deleteuser'),
    

]
