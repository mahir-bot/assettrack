from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.Signup, name='signup'),
    path('signin/', views.Signin, name='signin'),
    path('logout/', views.Signout, name='signout'),
    path('company/', views.CompanyList.as_view(), name='company-list'),
    path('user/', views.UserList.as_view(), name='user-list'),

]
