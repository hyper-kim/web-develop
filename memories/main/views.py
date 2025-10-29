from django.shortcuts import render, get_object_or_404, redirect
from django. contrib.auth.models import User
from django.contrib import auth
from django.db.models import Q
from crud.models import Addmemory, Photo
# Create your views here.
def showmain(request):
    memories = Addmemory.objects.order_by('-update_date')
    return render(request, 'mainpage.html', {'memories': memories})

# def search(request):
#     if request.method=='POST':
#         findkey=request.POST['findkey']
#         memories=Addmemory.objects.filter(title__icontains=findkey)
#         memories=Addmemory.objects.filter(body__icontains=findkey)
#         memories=Addmemory.objects.filter(user_tag__icontains=findkey)
#         memories=Addmemory.objects.filter(hash_tag__icontains=findkey)
#         return render(request, 'searched.html',{'searched':findkey,'memories':memories})
#     else:
#         return render(request,'searched.html',{})

def search(request):
    if request.method=='GET':
        search = request.GET.get('search')
        memories = Addmemory.objects.filter(Q(title__icontains = search) | Q(body__icontains = search) | Q(user_tag__icontains = search) | Q(hash_tag__icontains = search))
        return render(request, 'searched.html', {'search' : search, 'memories' : memories})