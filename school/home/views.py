from django.shortcuts import render
from .models import TopStudents, Post
from django.template.defaulttags import register


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

def homePage(request):
    rank1 = TopStudents.objects.filter(rank=1).order_by('grade')
    rank2 = TopStudents.objects.filter(rank=2).order_by('grade')
    rank3 = TopStudents.objects.filter(rank=3).order_by('grade')
    posts = Post.objects.filter(status=1).order_by('-created_on')
    context = {'rank1': rank1, 'rank2':rank2, 'rank3':rank3, 'posts':posts}
    return render(request, 'index.html', context=context)