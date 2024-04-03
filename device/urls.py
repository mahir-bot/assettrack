from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('all-log/',
         views.CompleteLogListAPIView.as_view(), name='all-log'),
    path('add-log/', views.AddDeviceLogList.as_view(), name='add-log'),


    # path('all-device-list', views.all_device_list, name='all-device-list'),
    # path('add-device/', views.add_device, name='add-device'),
    # path('update-device/<int:pk>/', views.update_device, name='update-device'),
    # path('delete-device/<int:pk>/', views.delete_device, name='delete-device'),

    path('device/', views.DeviceList.as_view(), name='device-list'),
    path('device-history/', views.DeviceListWithHistory.as_view(),
         name='device-history-list'),
    path('device-history/<int:pk>/',
         views.DeviceHistory.as_view(), name='device-history'),
    path('device/<int:pk>/', views.DeviceDetail.as_view(), name='device-detail'),





]
