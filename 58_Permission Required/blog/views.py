from django.shortcuts import render

from django.contrib.auth.decorators import permission_required

# Create your views here.

@permission_required('blog.can_edit')
def updateView(request):
	context = {
		'page_title':'Edit Artikel',
	}

	return render(request,'blog/edit.html',context)


# @permission_required('blog.add_artikel')
# @permission_required('blog.add_artikel',login_url='/admin/')
@permission_required('blog.add_artikel',login_url=None, raise_exception=True)
def addView(request):
	
	context = {
		'page_title':'Add Artikel',
	}

	return render(request,'blog/add.html',context)

def indexView(request):
	print(request.user.get_all_permissions())
	context = {
		'page_title':'Blog',
	}

	return render(request,'blog/index.html',context)