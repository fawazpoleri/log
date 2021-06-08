from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
# from accounts.forms import UserAdminCreationForm
from account.forms import UserAdminCreationForm



from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages


from django.contrib.auth.models import AbstractUser, BaseUserManager


from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Student , Staff

def login_view(request):
	if request.method == 'POST':
		email = request.POST.get('email')
		password = request.POST.get('password')

		user = authenticate(email=email,password=password)
		# user = auth.authenticate(request, username=request.POST.get('email'), password=request.POST.get('password'))

		if user is not None :
			auth.login(request,user)

			if user.is_student==True:
				# return HttpResponse("studenthome")				
				return redirect("studenthome")

			else:
				if user.is_superuser==True:
					return redirect("/admin")

				elif user.is_staffs==True:
					# return HttpResponse("staffhome")					
					return redirect("staffhome")

		else:

			messages.info(request,'invalid credential/account not active')
			return render(request,'account/login.html')

	else:
		return render(request,'account/login.html')





 
def staffhome(request):
    return render(request,'staff/staff_home.html')


def studenthome(request):
    return render(request,'student/student_home.html')

def  register(request):
	pass
