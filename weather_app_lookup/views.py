from django.shortcuts import render
# This is a comment to test git add
def home(request):
    return render(request, 'home.html', {})

def about(request):
    return render(request, 'about.html', {})