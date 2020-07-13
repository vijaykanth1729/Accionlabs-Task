from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import Http404
from .models import MyBlog
from .forms import BlogForm
from .serializers import MyBlogSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


def index(request):
    posts = MyBlog.objects.order_by('-updated')
    new_data = []
    for post in posts:
        if post.message == post.message[::-1]:
            new_data.append(post)
    context = {
        'posts':posts,
        'posts_new':new_data,
    }
    return render(request, 'blog/index.html', context)

def create(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Blog Post Creation Successfull.')
            return redirect('blog:home')
    else:
        form = BlogForm()
    return render(request, 'blog/create.html', {'form': form})

def update(request, id):
    post = MyBlog.objects.get(id=id)
    if request.method == "POST":
        form = BlogForm(request.POST or None, instance=post)
        if form.is_valid():
            form.save()
            messages.info(request, 'Blog Post Updation Successfull.')
            return redirect('blog:home')
    else:
        form = BlogForm(instance=post)
    return render(request, 'blog/update.html', {'form': form})

def detail(request, id):
    try:
        post = MyBlog.objects.get(id=id)
        context = {
            'post':post
            }
    except MyBlog.DoesNotExist:
        raise Http404

    return render(request, 'blog/detail.html', context)

def delete(request, id):
    post = MyBlog.objects.get(id=id)
    if request.method == "POST":
        post.delete()
        messages.warning(request, 'Post deleted successfull')
        return redirect('blog:home')
    return render(request, 'blog/delete.html', {'post':post})

def palindrome_check(request, id):
    post = MyBlog.objects.get(id=id)
    if post.message == post.message[::-1]:
        context = {
            'post': "This is a palindrome: "+ post.message
        }
    else:
        context = {
            'post': 'Current message is not a palindrome..',
        }
    return render(request, 'blog/palindrome_check.html', context)

class BlogList(APIView):
     def get(self, request, format=None):
        posts = MyBlog.objects.order_by('timestamp')
        serializer = MyBlogSerializer(posts, many=True)
        return Response(serializer.data)

     def post(self, request, format=None):
        serializer = MyBlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogDetail(APIView):
    """
    Retrieve, update or delete a blog instance.
    """
    def get_object(self, pk):
        try:
            return MyBlog.objects.get(pk=pk)
        except MyBlog.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = MyBlogSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = MyBlogSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
