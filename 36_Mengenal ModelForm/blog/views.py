from django.shortcuts import render, redirect

# Create your views here.
from .forms import PostForm
from .models import Post

def index(request):
	posts = Post.objects.all()

	context = {
		'page_title':'post list',
		'posts':posts
	}

	return render(request,'blog/index.html',context)

def create(request):
	post_form = PostForm(request.POST or None)
	if request.method == 'POST':
		if post_form.is_valid():
			post_form.save()

			return redirect('blog:index')

	context = {
		'page_title':'create post',
		'post_form' :post_form

	}
	return render(request,'blog/create.html',context)
