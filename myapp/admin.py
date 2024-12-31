from django.contrib import admin
from .models import*


# Register your models here.
class add_workeradmin(admin.ModelAdmin):
    list_display=["fullname"]

admin.site.register(addworker_model,add_workeradmin)
admin.site.register(addjob_model)
admin.site.register(contactmodel)

admin.site.register(signupmodel)

