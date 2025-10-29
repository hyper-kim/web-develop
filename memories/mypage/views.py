from django.shortcuts import render
from crud.models import Addmemory
# Create your views here.
def mypost(request):
        memories = Addmemory.objects.all()
        memories_list = memories.filter(username=request.user.username)
        return render(request, 'mypage.html', {'memories': memories}