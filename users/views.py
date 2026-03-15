from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login
from .models import User


@login_required
def redirect_after_login(request):
    return redirect(request.user.get_dashboard_url())


def is_admin(user):
    return user.is_authenticated and user.role == 'admin'


@user_passes_test(is_admin)
def add_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        role = request.POST.get("role")
        password = request.POST.get("password")

        if not username or not password or not role:
            messages.error(request, "Please fill all required fields!")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
        else:
            user = User.objects.create(
                username=username,
                email=email or '',
                role=role,
                password=make_password(password),
                is_active=True
            )
            messages.success(request, f"User '{username}' created successfully as {role}!")
            return redirect("manage_users")

    return render(request, "admin/add_user.html")


from core.models import Paper

@login_required
def submit_paper(request):
    if request.user.role != 'author':
        messages.error(request, "Only authors can submit papers.")
        return redirect(request.user.get_dashboard_url())

    if request.method == "POST":
        title = request.POST.get("title")
        abstract = request.POST.get("abstract")
        file = request.FILES.get("file")

        if not title or not abstract or not file:
            messages.error(request, "Please fill all fields and upload a PDF file.")
        else:
            Paper.objects.create(
                title=title,
                abstract=abstract,
                author=request.user,
                file=file,
            )
            messages.success(request, "Paper submitted successfully! Waiting for review.")
            return redirect("author_dashboard")

    return render(request, "author/submit_paper.html")


def register(request):
    if request.user.is_authenticated:
        return redirect(request.user.get_dashboard_url())

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if not username or not email or not password:
            messages.error(request, 'Please fill all fields.')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken.')
        elif password != confirm_password:
            messages.error(request, 'Passwords do not match.')
        else:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                role='participant'
            )
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('participant_dashboard')

    return render(request, 'registration/register.html')


def author_register(request):
    if request.user.is_authenticated:
        return redirect(request.user.get_dashboard_url())

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if not username or not email or not password:
            messages.error(request, 'Please fill all fields.')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken.')
        elif password != confirm_password:
            messages.error(request, 'Passwords do not match.')
        else:
            User.objects.create_user(
                username=username,
                email=email,
                password=password,
                role='author',
                is_active=False
            )
            messages.success(request, 'Registration submitted! Wait for admin approval.')
            return redirect('login')

    return render(request, 'registration/author_register.html')