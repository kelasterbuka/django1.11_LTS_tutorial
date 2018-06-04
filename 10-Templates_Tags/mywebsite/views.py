from django.shortcuts import render

def index(request):
	context = {
		'judul':'kelas terbuka',
		'subjudul':'selamat datang',
		'nav': [
			['/','Home'],
			['/blog','Blog'],
			['/about','About'],
			['/contact','Contact']
		]
	}
	return render(request,'index.html',context)





	