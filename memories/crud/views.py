from django.shortcuts import render, get_object_or_404, redirect
from django. contrib.auth.models import User
from django.contrib import auth
from django.utils import timezone
from .models import Addmemory, Photo
# Create your views here.
def create(request):
    if(request.method == 'POST'):
        user_id = request.POST.get('username', '')
        res_data = {}

        if not (request.POST['title'] and request.POST['hash_tag']):
            res_data['error'] = "제목 혹은 해시태그를 입력해주세요"
            return render(request, 'post.html', res_data)
        post = Addmemory()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.user_tag = request.POST['user_tag']
        post.hash_tag = request.POST['hash_tag']
        post.username = user_id
        post.upload_date = timezone.datetime.now()
        post.update_date = timezone.datetime.now()
        post.like=0
        post.report=0
        post.save()
        
        for img in request.FILES.getlist('pictures'):
            photo = Photo()
            photo.post = post
            photo.image = img
            photo.save()
            
            
        return redirect('/')
    return render(request, 'post.html') 

def detail(request,memories_id):
  post_detail = get_object_or_404(Post,pk=memories_id)
  comments = Comment.objects.filter(post = memories_id)
  if request.method == "POST":
    comment = Comment()
    comment.post = post_detail
    comment.body = request.POST['body']
    comment.date = timezone.now()
    comment.save()
  return render(request,'detail.html',{'post':post_detail, 'comments':comments})
