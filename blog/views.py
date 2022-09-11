from django.shortcuts import render
from django.views import generic
from .models import Post, Contact

# Create your views here.
# subclass ListView allows rendering a list with objects of models
class ListPost(generic.ListView):
    # filter allows only published statuses to be showen on the front end
    # - before created on allows latest post be shown
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class DetailsPost(generic.DetailView):
    model = Post
    template_name = 'details_post.html'

# function to render contact form
def Contact(request):
    if request.method=="POST":
        contact=Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        contact.name
        contact.email=email
        contact.subject=sunject
        
    return render(request, 'contact.html')    