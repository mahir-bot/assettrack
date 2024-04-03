from django.db import models
from account.models import Company
from django.contrib.auth import get_user_model


class Device(models.Model):
    DEVICE_LAPTOP = 'L'
    DEVICE_SMARTPHONE = 'S'
    DEVICE_TABLET = 'T'
    DEVICE_MONITOR = 'M'
    DEVICE_KEYBOARD = 'K'
    DEVICE_HEADSET = 'H'
    DEVICE_NULL = 'N'
    DEVICE_CHOICES = [
        (DEVICE_LAPTOP, 'Laptop'),
        (DEVICE_SMARTPHONE, 'Smartphone'),
        (DEVICE_TABLET, 'Tablet'),
        (DEVICE_MONITOR, 'Monitor'),
        (DEVICE_KEYBOARD, 'Keyboard'),
        (DEVICE_HEADSET, 'Headset'),
        (DEVICE_NULL, 'Null'),
    ]

    name = models.CharField(max_length=100, null=False, blank=False)
    serial_no = models.CharField(max_length=100, null=False, blank=False)
    model = models.CharField(max_length=100, null=False, blank=False)
    type = models.CharField(
        max_length=1, choices=DEVICE_CHOICES,)
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return f"{self.name} - {self.model} - {self.serial_no}"


class AddDeviceLog(models.Model):
    CHECKOUT = 'C'
    RETURN = 'R'
    CHOICES = [
        (CHECKOUT, 'Checked Out'),
        (RETURN, 'Returned'),
    ]
    User = get_user_model()
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    choice = models.CharField(max_length=1, choices=CHOICES)
    assigned_to = models.ForeignKey(
        User, on_delete=models.CASCADE)
    condition = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.device}  - {self.timestamp}"
