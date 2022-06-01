from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
# Create your views here.
from django.views import generic
from .models import Post


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

def admin_panel(request):
    return render(request,'admin_panel.html')