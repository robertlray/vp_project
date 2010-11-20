from django.template import Context, loader
from vp_project.models import Category, Video
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse

def index(request):
    category_list = Category.objects.all().order_by('-id_number')[:]
    return render_to_response('vp_project/index.html', {'category_list': category_list})

def category(request, category_id):
    category_list = Category.objects.all().order_by('-id_number')[:]
    c = get_object_or_404(Category, pk=category_id)
    return render_to_response('vp_project/category.html', {
            'category': c,
            'category_list': category_list,
    })

def video(request, video_id):
    v = get_object_or_404(Video, pk=video_id)
    return render_to_response('vp_project/video.html', {'video': v})

def about(request):
    return render_to_response('vp_project/about.html')

