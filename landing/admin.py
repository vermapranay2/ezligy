from django.contrib import admin
from .models import Register , Heads, Service, Single, Contact, Rti, ParalegalContact

# Register your models here.
admin.site.register(Register)
admin.site.register(Heads)
admin.site.register(Service)
admin.site.register(Contact)
admin.site.register(Single)
admin.site.register(Rti)
admin.site.register(ParalegalContact)

