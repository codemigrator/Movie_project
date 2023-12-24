from django.db.models import Q
from django.shortcuts import render, HttpResponse, redirect
from.models import Movie
from.forms import FormsMovies



def home(request):
    movie = Movie.objects.all()
    context ={
        'movie_list': movie
    }
    return render(request, 'movie.html', context)


def details(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, "details.html", {'movie': movie})


def add(request):
    if request.method == "POST":
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        img = request.FILES['img']
        movie = Movie(name=name,desc=desc,img=img)
        movie.save()

    return render(request, 'add.html')


def update(request,id):
    movie = Movie.objects.get(id=id)
    form= FormsMovies(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'movie':movie,'form':form})


def delete(request,id):
    if request.method == 'POST':
        movie = Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')


def search(request):
    query = None
    product = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        product = Movie.objects.all().filter(Q(name__contains=query)|Q(desc__contains=query))
        return render(request,'search.html',{'query':query,'product':product})