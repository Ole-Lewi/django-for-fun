from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

#def home(request):
    #return HttpResponse("Hello Lincoln, welcome to the Django blog!")

from django.shortcuts import render, redirect

from .models import Post

def home(request):
    posts = Post.objects.all().order_by('-created_at')  # Fetch all posts from the database
    return render(request, 'blog/home.html', {'posts': posts})  # Render the home template with posts

from .forms import PostForm

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new post to the database
            return redirect('home')  # Redirect to the home page after saving
    else:
        form = PostForm()  # Create a new form instance for GET requests

    return render(request, 'blog/create_post.html', {'form': form})  # Render the create post template with the form