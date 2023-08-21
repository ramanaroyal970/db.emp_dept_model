from django.db import models

# Create your models here.
class department(models.Model):
    dept_no=models.IntegerField(primary_key=True)
    dept_name=models.CharField(max_length=100)
    def __str__(self):
        return self.dept_name



class employee(models.Model):
    emp_id=models.IntegerField(primary_key=True)
    empname=models.CharField(max_length=100)
    salary=models.IntegerField()
    joindate=models.DateField()
    commission=models.IntegerField(null=True)
    dept_no=models.ForeignKey(department,on_delete=models.CASCADE)
    def __str__(self):
        return self.empname
