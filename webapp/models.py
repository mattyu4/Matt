from django.db import models

class Program(models.Model):
    program = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=50, null=True)
    started_date = models.DateField(null=True)

    def __str__(self):
        return self.program
    
class Member(models.Model):
    member_full_name = models.CharField(max_length=50, null=True)
    age = models.IntegerField(null=True)
    phone = models.IntegerField(blank=True)
    email = models.EmailField(blank=True)
    membership_number = models.AutoField(primary_key=True)
    date_created = models.DateTimeField(auto_now_add=True)
    program = models.ManyToManyField(Program)

    def __str__(self):
        return self.member_full_name
    
class Staff(models.Model):
    member = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name
    
class Price(models.Model):
    program = models.ForeignKey(Program, on_delete=models.SET_NULL, null=True)
    membership_price = models.IntegerField(blank=True)
    terms = models.TextField(blank=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)

    def __str__(self):
        return self.terms

class Status(models.Model):
    member = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True)
    price = models.OneToOneField(Price, on_delete=models.SET_NULL, null=True)
    
    STATUS = (
        ('A', 'Active'),
        ('I', 'Inactive'),
    )
    status = models.CharField(max_length=1, choices=STATUS)

    def __str__(self): return f"{self.member.member_full_name}'s Status for Contract {self.price.program.program}"