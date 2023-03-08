from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Post
from .form import PostForm


# Create your views here.
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': 'Tên người dùng đã tồn tại'})
        user = User.objects.create_user(username=username, email=email, password=password)
        return redirect('login')
    return render(request, 'signup.html', {'succeed': 'Đăng kí thành công'})


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Thông tin không hợp lệ'})
    return render(request, 'login.html')



def home(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        form = PostForm()
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
        context = {
            'posts': posts,
            'form': form
        }
        return render(request, 'home.html', context)
    else:
        return redirect('login')