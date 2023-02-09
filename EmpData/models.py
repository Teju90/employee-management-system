from django.db import models


class Position(models.Model):
    emp_position = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    
    def __str__(self):
        return self.emp_position


class Department(models.Model):
    dept_name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.dept_name
    



class Employee(models.Model):
    name = models.CharField(max_length=250)
    gender = models.CharField(max_length=50)
    dob = models.DateField()
    email = models.EmailField()
    phone_number = models.PositiveBigIntegerField()
    address = models.TextField()
    date_hired = models.DateTimeField(auto_now_add=True)
    salary = models.IntegerField()
    status = models.BooleanField(default=True)
    position = models.ForeignKey(Position , on_delete=models.CASCADE, related_name = 'position')
    dept = models.ForeignKey(Department , on_delete=models.CASCADE, related_name = 'deptname')

    def __str__(self):
        return self.name
    
    
    