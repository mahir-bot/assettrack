from rest_framework import serializers
from .models import Device, AddDeviceLog


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'


class AddDeviceLogSerializer(serializers.ModelSerializer):


    class Meta:
        model = AddDeviceLog
        fields = ['device', 'choice', 'condition',
                  'assigned_to', 'timestamp']

    def validate(self, data):
        # Get the device from the data dictionary
        device = data.get('device')
        existing_entries = AddDeviceLog.objects.filter(device=device)

        if existing_entries.exists():
            latest_entry = existing_entries.last()
            if latest_entry.choice == data['choice']:
                raise serializers.ValidationError(
                    f"Wrong Choice: {data['choice']}")

        return data
