from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, FormView, ListView
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class HomePageView(TemplateView):
    template_name = "feed/home.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['my_thing'] = "Hello world :P this is dynamic"
        ## order by id descending: minus sign 
        context['posts'] = Post.objects.all().order_by('-id')
        return context
    
class PostDetailView(DetailView):
    template_name = "feed/detail.html"
    model = Post

class AddPostView(LoginRequiredMixin, FormView):
    template_name = "feed/new_post.html"
    form_class = PostForm
    success_url = "/"

    ## IMPORTANT: Use this when you need to get "request"
    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)
        
    def form_valid(self, form):
        new_object = Post.objects.create(
            text=form.cleaned_data['text'],
            image=form.cleaned_data['image'],
            author = self.request.user
        )
        messages.add_message(self.request, messages.SUCCESS, "Your post was successful")
        return super().form_valid(form)
    
class ListPostsView(ListView):
    http_method_names = ["get"]
    template_name = "feed/list.html"
    model = Post
    context_object_name = "posts"
    queryset = Post.objects.all().order_by('-id')[0:12]