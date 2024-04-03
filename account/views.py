from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import User, Company
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, CompanySerializer


############## about the account ################

def Signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        try:
            if request.method == 'POST':
                company_name = request.POST.get("company_name")
                if company_name:
                    company, created = Company.objects.get_or_create(
                        name=company_name)
                else:
                    company_id = request.POST.get("company")
                    company = Company.objects.get(id=company_id)
                User.objects.create_user(
                    username=request.POST['username'],
                    email=request.POST["email"],
                    user_type=request.POST["user-type"],
                    password=request.POST["password"],
                    company=company
                )
                messages.success(request, 'Account created successfully')
                return redirect('signin')
        except Exception as e:
            print(e)
        companies = Company.objects.all()
        return render(request, 'account/signup.html', {'companies': companies})


def Signin(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            user = authenticate(
                email=request.POST["email"],
                password=request.POST['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid credentials')

        return render(request, 'account/signin.html', {})


@login_required(login_url='login')
def Signout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('home')


############ about the company ################


class CompanyList(ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated]


############ about the user ################

class UserList(ListCreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        company = user.company
        return User.objects.filter(
            company=company)


############ about the company Raw code ################

# @api_view(['POST'])
# def add_company(request):
#     serializer = CompanySerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)


# @api_view(['POST'])
# def update_company(request, pk):
#     company = Company.objects.get(id=pk)
#     serializer = CompanySerializer(instance=company, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)


# @api_view(['DELETE'])
# def delete_company(request, pk):
#     serializer = Company.objects.get(id=pk)
#     serializer.delete()
#     return Response(serializer.data)


# @api_view(['GET'])
# def all_company(request):
#     all_company = Company.objects.all()
#     serializer = CompanySerializer(all_company, many=True)
#     return Response(serializer.data)


############## about the user Raw code ################


# @api_view(['POST'])
# def add_user(request):
#     serializer = UserSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)


# @api_view(['POST'])
# def update_user(request, pk):
#     update_user = User.objects.get(id=pk)
#     serializer = UserSerializer(instance=update_user, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)


# @api_view(['DELETE'])
# def delete_user(request, pk):
#     serializer = User.objects.get(id=pk)
#     serializer.delete()
#     return Response(serializer.data)


# @api_view(['GET'])
# def view_user(request, pk):
#     view_user = User.objects.get(id=pk)
#     serializer = UserSerializer(view_user, many=False)
#     return Response(serializer.data)
