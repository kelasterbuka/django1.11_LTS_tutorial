from django.shortcuts import render

# Create your views here.


from .models import Post

def index(request):
	# queryset
	posts = Post.objects.all()
	context = {
		'Title':'Blog',
		'Heading':'Blog di my website',
		'Posts':posts,
	}

	return render(request,'blog/index.html',context)