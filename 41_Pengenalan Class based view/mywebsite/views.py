from django.shortcuts import render
from django.views import View

def index(request):
	context = {
		'heading':'SELAMAT DATANG',
	}

	if request.method == 'POST':
		context['heading'] = 'POST function based view'

	return render(request,'index.html',context)


class IndexClassView(View):

	template_name = ''
	context = {}

	# override method get dari parent class View
	def get(self,request):
		self.context['heading'] = 'GET class based view'
		return render(request,self.template_name,self.context)

	def post(self,request):
		self.context['heading'] = 'POST class based view'
		return render(request,self.template_name,self.context)


