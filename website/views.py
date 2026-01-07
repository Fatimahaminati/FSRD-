from django.shortcuts import render, get_object_or_404
from .models import Berita, Dosen, Akademik

def index(request):
    berita_list = Berita.objects.all().order_by('-tanggal')[:3]
    dosen_list = Dosen.objects.all()
    akademik_list = Akademik.objects.all()[:3]
    
    context = {
        'berita': berita_list,
        'dosen': dosen_list,
        'akademik': akademik_list,
    }
    return render(request, 'index.html', context)

def detail_berita(request, id):
    berita = get_object_or_404(Berita, id=id)
    return render(request, 'detail_berita.html', {'berita': berita})

def berita_list(request):
    berita_list = Berita.objects.all().order_by('-tanggal')
    return render(request, 'berita_list.html', {'berita': berita_list})

def dosen_list(request):
    dosen_list = Dosen.objects.all()
    return render(request, 'dosen_list.html', {'dosen': dosen_list})

def akademik(request):

    from .models import Akademik
    items = Akademik.objects.all()
    return render(request, 'akademik.html', {'items': items})

def akademik_detail(request, slug):
    from .models import Akademik
    from django.shortcuts import get_object_or_404
    obj = get_object_or_404(Akademik, slug=slug)
    return render(request, 'akademik_detail.html', {'item': obj})

def kontak(request):
    return render(request, 'kontak.html')