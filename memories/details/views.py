from django.shortcuts import render, get_object_or_404, redirect
from crud.models import Addmemory
# Create your views here.



def detail(request, memory_id):
    memories_detail = get_object_or_404(Addmemory, pk=memory_id)
    return render(request, 'detail.html', {'memory': memories_detail})

def delete(request, memory_id):
    memories = Addmemory.objects.get(pk = memory_id)
    memories.delete()
    return redirect('/')
    
def modify(request, memories_id):
    memories = memories.objects.get(pk = memories_id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=memories)
        if form.is_valid():
            post.title = form.POST['title']
            post.body = form.POST['body']
            post.user_tag = form.POST['user_tag']
            post.hash_tag = form.POST['hash_tag']
            post.username = user_id
            post.upload_date = timezone.datetime.now()
            post.update_date = timezone.datetime.now()
            post.save()
            return redirect('/')
    else:
        memories = memories.objects.get(pk = memories_id)