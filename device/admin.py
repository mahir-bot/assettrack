from django.contrib import admin
from .models import Device, AddDeviceLog


class AddDeviceLogAdmin(admin.ModelAdmin):
    list_display = ('device_details', 'choice', 'condition', 'timestamp')

    def device_details(self, obj):
        return f"{obj.device.name} - {obj.device.model} - {obj.device.serial_no}"
    device_details.short_description = 'Device Details'


class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'serial_no', 'model',
                    'type', 'company')


admin.site.register(AddDeviceLog, AddDeviceLogAdmin)
admin.site.register(Device, DeviceAdmin)
