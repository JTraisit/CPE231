from django.db import models
from django.db.models.fields import CharField, IntegerField
from django.db.models.fields.related import ForeignKey

# Create your models here.
class customer(models.Model):
    customer_id = models.CharField(primary_key=True,max_length=100)
    c_email = models.CharField(max_length=50)
    c_password = models.IntegerField(null= False)
    customer_name = models.CharField(max_length=50)
    c_tel = models.IntegerField(null=True,blank=True)
    def __self__(self):
        return self.customer_id



class service(models.Model):
    service_id = models.CharField(primary_key=True,max_length=100)
    customer_id = models.ForeignKey(customer,on_delete=models.CASCADE, db_column='customer_id')
    service_name = models.CharField(max_length=50)
    price = models.IntegerField()
    def __self__(self):
        return self.service_id

class schedule(models.Model):
    time = models.TimeField()
    customer_id = models.ForeignKey(customer,on_delete=models.CASCADE, db_column='customer_id')
    sch_id = models.CharField(primary_key=True,max_length=100)
    date = models.DateField()
    def __self__(self):
        return self.sch_id


class manager(models.Model):
    manager_id = CharField(primary_key=True,max_length=100)
    m_age = IntegerField(max_length=4)
    manager_name = CharField(max_length=50)
    def __self__(self):
        return self.manager_id

class employee(models.Model):
    employee_id = models.CharField(primary_key=True,max_length=100)
    sch_id = models.ForeignKey(schedule,on_delete=models.CASCADE, db_column='sch_id')
    manager_id = models.ForeignKey(manager,on_delete=models.CASCADE, db_column='manager_id')
    e_email = models.CharField(max_length=50)
    speciality = models.CharField(max_length=100)
    e_age = models.IntegerField()
    employee_name = models.CharField(max_length=100)
    salary = models.IntegerField(max_length=50)
    e_tel = models.CharField(max_length=50)
    e_password = models.IntegerField(null=False)
    def __self__(self):
        return self.employee_id



class employee_schedule(models.Model):
    e_sch_id = models.IntegerField(primary_key=True,max_length=100)
    time = models.TimeField()
    date = models.DateField()
    manager_id = models.ForeignKey(manager,on_delete=models.CASCADE, db_column='manage_id')
    sch_id = models.ForeignKey(employee,on_delete=models.CASCADE, db_column='sch_id')
    def __self__(self):
        return self.e_sch_id

class stock(models.Model):#น่าจะเป็น m to m ต้องแก้รอคุย
    stock_id = CharField(primary_key=True,max_length=100)
    service_id = models.ForeignKey(service,on_delete=models.CASCADE, db_column='sercice_id')
    manager_id = models.ForeignKey(manager,on_delete=models.CASCADE, db_column='manage_id')
    stock_name = CharField(max_length=50)
    stock_qty = CharField(max_length=100)
    def __self__(self):
        return self.stock_id
     


    





