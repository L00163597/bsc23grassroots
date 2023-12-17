from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegistrationForm


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log the user in after registration
            # Redirect to a success page.
            return redirect(
                'home')  # Replace 'index' with the name of the view that should be displayed on successful registration
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})
