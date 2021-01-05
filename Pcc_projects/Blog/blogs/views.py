from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import BlogPost
from .forms import BlogPostForm


def index(request):
    """The home page for blog"""
    return render(request, 'blogs/index.html')


@login_required
def posts(request):
    """Show all posts."""
    posts = BlogPost.objects.filter(owner=request.user).order_by('date_added')

    context = {'posts': posts}
    return render(request, 'blogs/posts.html', context)


@login_required
def new_post(request):
    """Add a new topic."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = BlogPostForm()
    else:
        # POST data submitted; process data.
        form = BlogPostForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            form.save()
            return HttpResponseRedirect(reverse('blogs:posts'))

    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)
