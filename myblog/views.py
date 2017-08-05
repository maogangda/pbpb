from django.shortcuts import render
from models import Article
# Create your views here.


def index(req):
    Arts=Article.objects.all()
    return render(req,'index.html',{'Arts':Arts})

def show(req,id):
    Art=Article.objects.get(pk=id)
    return render(req,'show.html',{'Art':Art})

def edit(req,id):
    if str(id)=='0':
        return render(req,'edit.html')
    Art=Article.objects.get(pk=id)
    return render(req,'edit.html',{'Art':Art})

def editAction(req):
    id=req.POST.get('id')
    tit=req.POST.get('title')
    con=req.POST.get('content')
    if str(id)=='0':
        Article.objects.create(title=tit,content=con)
    else:
        art=Article.objects.get(pk=id)
        art.title=tit
        art.content=con
        art.save()
    arts=Article.objects.all()
    return render(req,'index.html',{'Arts':arts})
