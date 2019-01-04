from django.shortcuts import render

from .forms import AllFormField
def index(request):
    context = {
        'heading':'Home',
        'allFormField':AllFormField(),
    }

    return render(request,'index.html',context)