from django.db import models
from django.db.models.fields import CharField, IntegerField
from django.db.models.fields.related import ForeignKey

# Create your models here.
class customer():
    customer_id = models.ForeignKey(primary_key=True)
    c_email = models.CharField(max_length=50)
    c_password = models.IntegerField(null= False)
    customer_name = models.CharField(max_length=50)
    c_tel = models.IntegerField(null=True,blank=True)

class service():
    service_id = models.OneToOneField(primary_key=True)
    customer_id = models.ForeignKey(customer,on_delete=models.CASCADE, db_column='customer_id')
    service_name = models.CharField(max_length=50)
    price = models.IntegerField()

class schedule():
    time = models.TimeField()
    customer_id = models.ForeignKey(customer,on_delete=models.CASCADE, db_column='customer_id')
    sch_id = models.ForeignKey(primary_key=True)
    date = models.DateField()
class manager():
    manager_id = ForeignKey(primary_key=True)
    m_age = IntegerField(max_length=4)
    manager_name = CharField(max_length=50)

class employee():
    employee_id = models.ForeignKey(primary_key=True)
    sch_id = models.ForeignKey(schedule,on_delete=models.CASCADE, db_column='sch_id')
    manager_id = models.ForeignKey(manager,on_delete=models.CASCADE, db_column='manager_id')
    e_email = models.CharField(max_length=50)
    speciality = models.CharField(max_length=100)
    e_age = models.IntegerField()
    employee_name = models.CharField(max_length=100)
    salary = models.IntegerField(max_length=50)
    e_tel = models.CharField(max_length=50)
    e_password = models.IntegerField(null=False)



class employee_schedule():
    e_sch_id = models.IntegerField()
    time = models.TimeField()
    date = models.date
    manager_id = models.ForeignKey(manager,on_delete=models.CASCADE, db_column='manage_id')
    sch_id = models.ForeignKey(employee,on_delete=models.CASCADE, db_column='sch_id')

class stock():#น่าจะเป็น m to m ต้องแก้รอคุย
    stock_id = ForeignKey(primary_key=True)
    service_id = models.ForeignKey(service,on_delete=models.CASCADE, db_column='sercice_id')
    manager_id = models.ForeignKey(manager,on_delete=models.CASCADE, db_column='manage_id')
    stock_name = CharField(max_length=50)
    stock_qty = CharField(max_length=100) 


    





