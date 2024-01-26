from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from blog.models import Blog


# Create your views here.
class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'body', 'preview', 'date_of_creation',)
    success_url = reverse_lazy('blog:list')


class BlogListView(ListView):
    model = Blog


class BlogDetailView(DetailView):
    model = Blog


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'body', 'preview', 'date_of_creation',)
    success_url = reverse_lazy('blog:list')


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:list')
