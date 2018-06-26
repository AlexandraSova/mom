from django.shortcuts import render

def home_page(request):
    return render(request, 'home/home_page.html', {})

def about(request):
    return render(request, 'home/about.html', {})

def rewards(request):
    return render(request, 'home/rewards.html', {})

def news(request):
    return render(request, 'home/news.html', {})