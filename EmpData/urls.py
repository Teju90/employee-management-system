from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('login/', login_user, name="login"),
    path('department/', Dept_List, name='department'),
    path('add_dept/', Add_Dept, name='add_dept'),
    path('del_dept/<int:id>', Delete_Dept, name='del_dept'),
    path('update_dept/<int:id>', Edit_Dept, name='update_dept'),
    path('employee/', Emp_List, name='employee'),
    path('add_emp/', Add_Emp, name='add_emp'),
    path('update_emp/<int:id>', Edit_Emp, name='update_emp'),
    path('del_emp/<int:id>', Delete_Emp, name='del_emp'),
    path('position/', Position_List, name='position'),
    path('add_posi/', Add_Posi, name='add_posi'),
    path('del_posi/<int:id>', Delete_Posi, name='del_posi'),
    path('update_posi/<int:id>', Edit_Posi, name='update_posi'),
    path('emp_details/<int:id>', Emp_Details, name="emp_details"),
    path('emp_posi/<int:id>', Emp_posi, name="emp_position"),
    path("logout/", logoutuser , name="logout"),

]