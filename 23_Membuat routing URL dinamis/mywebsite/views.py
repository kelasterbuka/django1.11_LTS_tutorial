from django.http import HttpResponse


def link(request,page):
	str = "<h1>{}</h1>".format(page)
	return HttpResponse(str)

def index(request):
	return HttpResponse("<h1>HOME</h1>")

def angka(request,input):

	heading = "<h1> Page Angka </h1>"
	str = heading + input
	return HttpResponse(str)

def tanggal(request,**input):
	print(input)
	tahun = input['tahun']
	bulan = input['bulan']
	hari = input['hari']
	heading = "<h1> Page Tanggal </h1>"
	dataTanggal = "<h2>{}/{}/{}</h2>".format(tahun,bulan,hari)
	return HttpResponse(heading + dataTanggal)

# def tanggal(request,tahun,bulan,hari):

# 	heading = "<h1> Page Tanggal </h1>"
# 	strTahun = "tahun: " + tahun
# 	strBulan = "bulan: " + bulan
# 	strHari = "hari: " + hari
# 	str = heading + strTahun + "<br>" + strBulan + "<br>" + strHari
# 	return HttpResponse(str)