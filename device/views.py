from rest_framework.generics import ListCreateAPIView
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .models import AddDeviceLog, Device
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import DeviceSerializer, AddDeviceLogSerializer
from rest_framework.views import APIView
# Create your views here.


# @login_required(login_url='login')
def home(request):
    return render(request, 'home.html')


#### about Log code ##########

class CompleteLogListAPIView(ListAPIView):
    serializer_class = AddDeviceLogSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        company = user.company
        devices = Device.objects.filter(company=company)
        device_ids = devices.values_list('id', flat=True)
        return AddDeviceLog.objects.filter(device__in=device_ids)


class AddDeviceLogList(ListCreateAPIView):
    serializer_class = AddDeviceLogSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        company = user.company
        device_ids = Device.objects.filter(
            company=company).values_list('id', flat=True)
        return AddDeviceLog.objects.filter(device__in=device_ids)


###### about device ##########


class DeviceList(ListCreateAPIView):
    serializer_class = DeviceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        company = user.company
        return Device.objects.filter(company=company)

    def create(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            company = user.company
            requested_company_id = request.data.get('company')
            if requested_company_id and requested_company_id != company.id:
                return Response(
                    {"error": "You can only add devices for your own company."},
                    status=status.HTTP_403_FORBIDDEN
                )
            return super().create(request, *args, **kwargs)
        else:
            return Response(
                {"error": "You must be authenticated and have a profile to add devices."},
                status=status.HTTP_403_FORBIDDEN
            )


class DeviceDetail(RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [IsAuthenticated]


class DeviceHistory(APIView):
    def get(self, request, pk):
        device_history = AddDeviceLog.objects.filter(device_id=pk)
        return render(request, 'device/device_history.html', {'device_history': device_history})


class DeviceListWithHistory(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        company = request.user.company
        devices = Device.objects.filter(company=company)
        all_device_data = []
        for device in devices:
            device_data = {
                'device_name': device.name,
                'device_serial': device.serial_no,
                'device_model': device.model,
                'device_type': device.type,
                'company': device.company.name,
                'device': device.pk,
            }
            all_device_data.append(device_data)
        return render(request, 'device/all_device.html', {'all_device_data': all_device_data})

######## about Log raw code ##########

# @api_view(['GET'])
# def show_complete_log(request, pk):
#     user = User.objects.get(id=pk)
#     company = user.company
#     devices = Device.objects.filter(company=company)
#     device_ids = devices.values_list('id', flat=True)
#     complete_log = AddDeviceLog.objects.filter(device__in=device_ids)
#     serializer = AddDeviceLogSerializer(complete_log, many=True)
#     print(serializer)
#     return Response(serializer.data)

########  Device Raw code  ###########

# @api_view(['POST'])
# def add_device_log(request):
#     add_device_log = AddDeviceLogSerializer(data=request.data)
#     if add_device_log.is_valid():
#         add_device_log.save()
#     return Response(add_device_log.data)


# @api_view(['GET'])
# def all_device_list(request):
#     all_device_list = Device.objects.all()
#     serializer = DeviceSerializer(all_device_list, many=True)
#     return Response(serializer.data)

# @api_view(['POST'])
# def add_device(request):
#     add_device = DeviceSerializer(data=request.data)
#     if add_device.is_valid():
#         add_device.save()
#     return Response(add_device.data)

# @api_view(['GET'])
# def show_device_detail(request, pk):
#     show_device_detail = Device.objects.filter(id=pk)
#     serializer = DeviceSerializer(show_device_detail, many=True)
#     return Response(serializer.data)


# @api_view(['POST'])
# def update_device(request, pk):
#     device = Device.objects.get(id=pk)
#     serializer = DeviceSerializer(instance=device, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)


# @api_view(['DELETE'])
# def delete_device(request, pk):
#     serializer = Device.objects.get(id=pk)
#     serializer.delete()
#     return Response(serializer.data)
