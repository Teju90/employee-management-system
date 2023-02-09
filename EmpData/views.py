from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth import authenticate, login, logout
# import json
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
# just created by me
# new added
@login_required(login_url="/login/")
def index(request):
    return render(request, 'home.html')

@login_required(login_url="/login/")
def Dept_List(request):
    depts = Department.objects.all()
    context = {
        'depts' : depts
    }
    return render(request, 'department.html', context)

@login_required(login_url="/login/")
def Add_Dept(request):
    if request.method =='POST':
        dept_name = request.POST['dept_name']
        description = request.POST['description']
        # status = request.POST['status']

        new_dept = Department(dept_name=dept_name, description=description)
        new_dept.save()

        return redirect('department')
    elif request.method == 'GET':
        return render(request, 'add_dept.html')
    else:
        return HttpResponse("An Exception Occured! Department is Not Been Added")

@login_required(login_url="/login/")
def Delete_Dept(request , id):
    dept = Department.objects.get(id=id)
    dept.delete()
    return redirect('department')

@login_required(login_url="/login/")
def Edit_Dept(request, id):
    dept = Department.objects.get(id=id)

    if request.method == 'POST':
        dept.dept_name = request.POST.get('dept_name')
        dept.description = request.POST.get('description')
        # dept.status = request.POST.get['status']
        dept.save()

        return redirect('department')
    
    return render(request, 'update_dept.html', {'dept' : dept}) 

@login_required(login_url="/login/")
def Emp_List(request):
    emps = Employee.objects.all()
    context = {
        'emps' : emps
    }
    return render(request, 'employee.html', context)

@login_required(login_url="/login/")
def Emp_Details(request, id):
    try:
        employee = Employee.objects.get(id=id)
    except Employee.DoesNotExist:
        employee = None

    context = {'employee': employee}
    return render(request, 'employee_details.html', context)

@login_required(login_url="/login/")
def Add_Emp(request):
    if request.method =='POST':
        name1 = request.POST['name']
        gender = request.POST['gender'] #--
        dob = request.POST['dob'] #--
        email = request.POST['email'] #--
        phone_number = request.POST['phone_number'] 
        address = request.POST['address']
        date_hired = request.POST['date_hired'] 
        salary = request.POST['salary']
        position = request.POST['position']
        dept=request.POST['dept']

        new_emp = Employee(name=name1,
                           gender=gender,
                           dob=dob,
                           email=email,
                           phone_number=phone_number,
                           address=address,
                           date_hired=date_hired,
                           salary=salary,
                           position_id=position,
                           dept_id=dept)
        new_emp.save()

        return redirect('employee')
    dpt = Department.objects.all()
    pos= Position.objects.all()

    return render(request, 'add_emp.html',{'pos':pos,'dpt':dpt})
    
    
@login_required(login_url="/login/")
def Edit_Emp(request, id):
    emp = Employee.objects.get(id=id)
    dpt = Department.objects.all()
    pos = Position.objects.all()

    if request.method == 'POST':
        emp.name = request.POST.get('name')
        emp.gender = request.POST.get('gender')
        emp.dob = request.POST.get('dob')
        emp.email = request.POST.get('email')
        emp.phone_number = request.POST.get('phone_number')
        emp.address = request.POST.get('address')
        emp.date_hired = request.POST.get('date_hired')
        emp.salary = request.POST.get('salary')
        emp.position_id = request.POST.get('position')
        emp.dept_id=request.POST.get('dept')
        emp.save()

        return redirect('index')

    
    return render(request, 'update_emp.html', {'emp' : emp,'dpt':dpt, 'pos':pos}) 

@login_required(login_url="/login/")
def Delete_Emp(request , id):
    emp= Employee.objects.get(id=id)
    emp.delete()
    return redirect('employee')

@login_required(login_url="/login/")
def Position_List(request):
    posi = Position.objects.all()
    context = {
        'posi' : posi
    }
    return render(request , 'position.html', context)

@login_required(login_url="/login/")
def Emp_posi(request,id):
    empl=Employee.objects.filter(position_id=id)

    pos=Position.objects.get(id=id).emp_position
    return render(request,'emp_posi.html',{'empl':empl,"pos":pos})

@login_required(login_url="/login/")
def Add_Posi(request):
    if request.method == 'POST':
        emp_position = request.POST['emp_position']
        description = request.POST['description']

        new_posi = Position(emp_position=emp_position,description=description) 
        new_posi.save()

        return redirect('position')

    
    return render(request, 'add_posi.html')

@login_required(login_url="/login/")
def Delete_Posi(request , id):
    posi = Position.objects.get(id=id)
    posi.delete()
    return redirect('position')

@login_required(login_url="/login/")
def Edit_Posi(request, id):
    posi = Position.objects.get(id=id)

    if request.method == 'POST':
        posi.emp_position = request.POST.get('emp_position')
        posi.description = request.POST.get('description')
        posi.save()
        return redirect('position')
    
    return render(request, 'update_posi.html', {'Posi':posi})


#login
def login_user(request):
    if request.method == "POST":
    
        user = authenticate(username=request.POST.get('username'),password=request.POST.get('password'))

        if user is not None:
            if user.is_active:
                auth.login(request, user)
                return redirect("/")
        else:
            return redirect('login')
    return render(request, "login.html")

    
#Logout
def logoutuser(request):
    logout(request)
    return redirect('login')

