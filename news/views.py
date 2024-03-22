from django.shortcuts import render
from .models import News

def news(request):
    oNews = News.objects.all()
    return render(request, 'news.html', {'vloNews': oNews})
