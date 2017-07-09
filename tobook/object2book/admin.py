from django.contrib import admin
from object2book.models import(
    Statuses,
    Location,
    Object,
)
# Register your models here.
class ObjectAdmin(admin.ModelAdmin):
    list_display = ('name','code','location','status','capacity','remaining',)

admin.site.register(Statuses)

admin.site.register(Location)

admin.site.register(Object, ObjectAdmin)
