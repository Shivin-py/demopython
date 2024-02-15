from django.shortcuts import render, redirect, get_object_or_404
from .forms import EditProfileForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


def user(request):
    return render(request, 'profile.html')


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile:profile')
    else:
        form = EditProfileForm(instance=request.user)
        return render(request, 'editprofile.html', {'form': form})


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('profile:profile')
        else:
            return redirect('profile:profile')
    else:
        form = PasswordChangeForm(user=request.user)
        return render(request, 'changepassword.html', {'form': form})
