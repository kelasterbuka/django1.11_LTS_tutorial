from django.http import HttpResponse

# method view index
def index(request):

	judul = "<h1> ini adalah Home </h1>"
	subjudul = "<h2> selamat datang di website ini </h2>"

	output = judul + subjudul;
	return HttpResponse(output)

def about(request):
	return HttpResponse("<h1> ini adalah About </h1>")