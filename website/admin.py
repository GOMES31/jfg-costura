from django.contrib import admin

from .models import Machine, MachineImage, Partner

# Register your models here.
@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display =  'order', 'name', 'image', 'active',
    list_editable = 'active',
    readonly_fields = 'order',

class MachineImageInLine(admin.TabularInline):
    model = MachineImage
    extra = 1
    fields = ['image']

@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    list_display = 'order', 'name', 'description',
    readonly_fields = 'order',
    inlines = [MachineImageInLine]