from django.contrib import admin
from .models import Program, Member, Staff, Price, Status

admin.site.register(Program)
admin.site.register(Member)
admin.site.register(Staff)
admin.site.register(Price)
admin.site.register(Status)