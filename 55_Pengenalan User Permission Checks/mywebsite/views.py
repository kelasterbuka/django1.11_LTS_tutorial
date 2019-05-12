from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# view method dengan internal permission checks
def index(request):
	context = {
		'page_title': 'Home',
	}

	print(request.user.is_authenticated())

	template_name = None
	if request.user.is_authenticated():
		# logika untuk user
		template_name = 'index_user.html'
	else:
		# logika untuk anonymous
		template_name = 'index_anonymous.html'
	
	return render(request, template_name, context)


def loginView(request):
	context = {
		'page_title':'LOGIN',
	}
	user = None

	if request.method == "GET":
		if request.user.is_authenticated():
			# logika untuk user
			return redirect('index')
		else:
			# logika untuk anonymous
			return render(request, 'login.html', context)


	if request.method == "POST":
		
		username_login = request.POST['username']
		password_login = request.POST['password']
		
		user = authenticate(request, username=username_login, password=password_login)

		if user is not None:
			login(request, user)
			return redirect('index')
		else:
			return redirect('login')
	
	
@login_required
def logoutView(request):
	context = {
		'page_title':'logout'
	}

	if request.method == "POST":
		if request.POST["logout"] == "Submit":
			logout(request)

		return redirect('index')	


	return render(request, 'logout.html', context)













