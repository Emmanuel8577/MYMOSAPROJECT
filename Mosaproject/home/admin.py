from django.contrib import admin
from home.models import registerMosa, contact_View


#Register your models here.
admin.site.register([registerMosa, contact_View])
