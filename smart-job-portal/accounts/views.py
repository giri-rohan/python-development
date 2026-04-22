
from django.shortcuts import render, redirect
from .forms import UserRegisterForm,Profileforms
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        profile_form = Profileforms(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            messages.success(request, "Account created successfully!")
            return redirect('login')
    else:
        user_form = UserRegisterForm()
        profile_form = Profileforms()

    return render(request, 'accounts/register.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

# Create your views here.
