from django.contrib import admin

# importing model
from collection.models import Thing

# set up automated slug creation
class ThingAdmin(admin.ModelAdmin):
    model = Thing
    list_displays = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}

# Register your models here.
admin.site.register(Thing, ThingAdmin)
