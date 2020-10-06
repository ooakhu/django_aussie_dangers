from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Spider
# Create your views here.

def loginx(request):
    spiders = Spider.objects
    return render(request,'spiders/index.html', {'spiders':spiders})

def detail (request, spider_id):
    spider_detail = get_object_or_404(Spider,pk=spider_id)
    return render(request, 'spiders/detail.html', {'spider':spider_detail})