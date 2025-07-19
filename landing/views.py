from django.shortcuts import render, redirect

def welcome(request):
    if request.user.is_authenticated:
        return redirect('dashboard') 
    return render(request, 'landing.page.html')
