from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name

class Auto_Year(models.Model):
    new = models.CharField(max_length=200)
    old = models.CharField(max_length=200)

    def __str__(self):
        return self.new

# class Avto(models.Model):
#     model = models.CharField(max_length=200)
#     name = models.ForeignKey(Category, on_delete=models.CASCADE)
#     avto_year = models.ForeignKey(Auto_Year,on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='avto')
#     mesta = models.CharField(max_length=10)
#     size = models.CharField(max_length=200)
#     massa = models.IntegerField()
#     rasxod = models.CharField(max_length=200)
#     transmissiya = models.CharField(max_length=100)
#     price = models.CharField(max_length=250)

#     def __str__(self):
#         return self.model


class Cars(models.Model):
    image = models.ImageField()
    myname = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    mesta = models.IntegerField()
    size = models.CharField(max_length=50)
    massa = models.IntegerField()
    rasxod = models.CharField(max_length=20)
    tranmissiya = models.CharField(max_length=50)
    price = models.CharField(max_length=250)

    
    
    def __str__(self):
        return self.myname


class Zakaz(models.Model):
    username = models.CharField(max_length=50)
    phonenumber = models.CharField(max_length=50)
    carname = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class AboutCompany(models.Model):
    title = models.CharField(max_length=200)
    about = RichTextField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Client_Corporativ(models.Model):
    sms = RichTextField()
    talk = RichTextField()

    def __str__(self):
        return self.sms

class Special_Client(models.Model):
    text = RichTextField()

    def __str__(self):
        return self.text

class Service_Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Service_xizmat(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Service_Category,on_delete=models.CASCADE)
    text = RichTextField()
    nomer = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Zapisatsiya(models.Model):
    title = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    dam = models.CharField(max_length=20)
    consultant = models.CharField(max_length=30)

class Zapisatsiya_form(models.Model):
    myname = models.CharField(max_length=100)
    myphone = models.CharField(max_length=100)
    model = models.CharField(max_length=30)

    def __str__(self):
        return self.myname

class Zapcharst(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.title


class Zapchast_zakas(models.Model):
    title = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    dam = models.CharField(max_length=20)
    consultant = models.CharField(max_length=30)

    def __str__(self):
        return self.title

class Zapchast_form(models.Model):
    myname = models.CharField(max_length=100)
    myphone = models.CharField(max_length=100)
    model = models.CharField(max_length=30)

    def __str__(self):
        return self.myname

class Guarantee(models.Model):
    title = models.CharField(max_length=200)
    text = RichTextField()

    def __str__(self):
        return self.title


# class SmallCars(models.Model):
#     image = models.ImageField()
#     mytitle = models.CharField(max_length=50)
    

#     def __str__(self):
#         return self.mytitle


# class CommericalCars(models.Model):
#     image = models.ImageField()
#     c_title = models.CharField(max_length=50)
    
#     def __str__(self):
#         return self.c_title



# class TruckCars(models.Model):
#     image = models.ImageField()
#     t_title = models.CharField(max_length=50)
    
#     def __str__(self):
#         return self.t_title


# class BusCars(models.Model):
#     image = models.ImageField()
#     b_title = models.CharField(max_length=50)
    
#     def __str__(self):
#         return self.b_title





# class ProbegCars(models.Model):
#     image = models.ImageField()
#     p_title = models.CharField(max_length=50)
#     pc = models.IntegerField()
    
#     def __str__(self):
#         return self.p_title









    


















