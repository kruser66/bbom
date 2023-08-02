from rest_framework import viewsets
from rest_framework import permissions

from django.contrib.auth import views as auth_views
from django.contrib.auth import authenticate, login
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from blog.models import User, Post
from blog.forms import Login, Post as PostForm
from blog.serializers import UserSerializer, PostSerializer
from blog.permissions import IsUserOrReadOnly


def index(request): #TODO переделать инифицированно на классы
    
    context = {}
    context['users'] = User.objects.all()
    
    return render(request, 'index.html', context=context)


def posts(request, id=None): #TODO переделать инифицированно на классы
    
    context = {}
    if id:
        posts_user = get_object_or_404(User, id=id)
        context['posts'] = Post.objects.filter(user=posts_user)
        context['username'] = posts_user.name
    else:
        context['posts'] = Post.objects.all()
    
    return render(request, 'posts.html', context=context)


@login_required(login_url='login')
def delete_post(request, id): #TODO переделать инифицированно на классы
    if id:
        Post.objects.filter(id=id).delete()
        return redirect('posts')


class LoginView(View):
    def get(self, request, *args, **kwargs):
        form = Login()
        return render(request, "login.html", context={
            'form': form
        })

    def post(self, request):
        form = Login(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                if request.GET.get('next'):
                    return redirect(request.GET.get('next'))
                return redirect("index")

        return render(request, "login.html", context={
            'form': form,
            'ivalid': True,
        })


class LogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('index')


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint all users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
        

class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint user's posts.
    """

    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsUserOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):

        if self.request.user.is_authenticated:
           return self.request.user.posts.all()            
        else:
           return {}
       
       
class PostView(View):
    def get(self, request, *args, **kwargs):
        form = PostForm()
        return render(request, "create_post.html", context={
            'form': form
        })

    def post(self, request):
        form = PostForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            body = form.cleaned_data['body']
            Post.objects.create(
                user=request.user,
                title=title,
                body=body
            )
            
            return redirect('posts')


        return render(request, "create_post.html", context={
            'form': form,
        })    