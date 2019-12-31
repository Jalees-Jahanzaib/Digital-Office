from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Files

def home(request):
    context={
        'Files': Files.objects.all()
    }
    
    return render(request,"blog/home.html",context)
class FileListView(ListView):
    model= Files
    template_name = 'blog/home.html'
    context_object_name= 'Files'
    ordering = ['-date_posted']
class FileDetailView(DetailView):
    model=Files

class FileCreateView(CreateView):
    model=Files
    fields=['title','summary']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



       
def about(request): 
    return render(request,"blog/about.html")
