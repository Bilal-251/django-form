from django.shortcuts import render

# Create your views here.
# def home(request):
#     return render(request,'home.html')

# views.py

from django.shortcuts import render, redirect
from .forms import UserProfileForm

def home(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Replace 'login_success' with the URL or name you want to redirect to upon successful login
    else:
        form = UserProfileForm()

    return render(request, 'home.html', {'form': form})
