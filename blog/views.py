from django.shortcuts import render
from django.views.generic import ListView, DetailView,TemplateView
from .models import Post

# Create your views here.

# Class based views

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-date_posted']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'


class AboutView(TemplateView):
    template_name = 'about.html'

# Function based views

# def home(request):
#     return render(request, 'home.html', {posts: Post.objects.all()})

# def article_detail(request, id):
#     return render(request, 'post.html', {posts: Post.objects.get(id=id)}
# def about(request):
#     return render(request, 'about.html', {})