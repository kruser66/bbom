from django.shortcuts import render, redirect

from rest_framework import viewsets
from rest_framework import permissions

from django.contrib.auth import views as auth_views
from django.contrib.auth import authenticate, login
from django.views import View
from django.urls import reverse_lazy

from blog.models import User, Post
from blog.forms import Login
from blog.serializers import UserSerializer, PostSerializer
from blog.permissions import IsUserOrReadOnly



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
                return redirect("index")

        return render(request, "login.html", context={
            'form': form,
            'ivalid': True,
        })


class LogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('index')


def index(request):
    
    context = {}
    context['users'] = User.objects.all()
    
    return render(request, 'index.html', context=context)


def posts(request):
    
    context = {}
    context['posts'] = Post.objects.all()
    
    return render(request, 'posts.html', context=context)


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