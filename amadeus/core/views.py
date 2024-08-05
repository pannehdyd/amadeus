from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(" **** before authentication ")
        user = authenticate(request, username=username, password=password)
        print(" ***** user = ", user)
        if user is not None:
            login(request, user)
            print("**** redirected to home ***** ")
            return redirect('home')  # Remplacez 'home' par l'URL vers laquelle vous souhaitez rediriger l'utilisateur après la connexion
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect')
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']
        if password == password_confirm:
            try:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                messages.success(request, 'Inscription réussie. Vous pouvez maintenant vous connecter.')
                return redirect('login')
            except Exception as e:
                messages.error(request, f'Erreur lors de l\'inscription: {e}')
        else:
            messages.error(request, 'Les mots de passe ne correspondent pas')
    return render(request, 'register.html')

# core/views.py

def home_view(request):
    return render(request, 'home.html')  # Assurez-vous que le template 'home.html' existe
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test

# Check if user is admin
def is_admin(user):
    return user.is_superuser

@login_required
@user_passes_test(is_admin)
def add_admin_view(request):
    if request.method == 'POST':
        usernames = request.POST.get('usernames').split(',')
        for username in usernames:
            username = username.strip()
            try:
                user = User.objects.get(username=username)
                user.is_staff = True
                user.is_superuser = True
                user.save()
                messages.success(request, f'{username} has been added as an admin.')
            except User.DoesNotExist:
                messages.error(request, f'{username} does not exist.')
        return redirect('add_admin')  # Redirect back to add admin page
    return render(request, 'core/add_admin.html')

@login_required
@user_passes_test(is_admin)
def remove_admin_view(request):
    if request.method == 'POST':
        usernames = request.POST.get('usernames').split(',')
        for username in usernames:
            username = username.strip()
            try:
                user = User.objects.get(username=username)
                user.is_staff = False
                user.is_superuser = False
                user.save()
                messages.success(request, f'{username} has been removed as an admin.')
            except User.DoesNotExist:
                messages.error(request, f'{username} does not exist.')
        return redirect('remove_admin')  # Redirect back to remove admin page
    return render(request, 'core/remove_admin.html')






