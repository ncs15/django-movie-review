from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
import requests
from django.conf import settings
import datetime
from django.core.paginator import Paginator
from django.db.models import Q

from movies.models import Collection, Comment,Quiz





# Create your views here.
def home(request):
    movies = Collection.objects.filter(popular=False,coming_next=False).order_by('-date_added')

    popular = Collection.objects.filter(popular=True).order_by('-date_added')

    coming_next = Collection.objects.filter(coming_next=True).order_by('-date_added')

    latest_1 = movies[0:4]
    latest_2 = movies[4:8]
    latest_3 = movies[8:12]
    popular_1 = popular[0:3]
    popular_2 = popular[3:6]
    popular_3 = popular[6:9]
    coming_next1 = coming_next[0:3]
    coming_next2 = coming_next[3:6]
    coming_next3 = coming_next[6:9]

    quiz = Quiz.objects.all()[int(datetime.datetime.now().strftime("%d"))]


    context={"quiz":quiz,"latest_1":latest_1,"latest_2":latest_2,"latest_3":latest_3,"popular_1":popular_1,"popular_2":popular_2,"popular_3":popular_3,"coming_next1":coming_next1,"coming_next2":coming_next2,"coming_next3":coming_next3}

    return render(request, "movies/home2.html",context)


def movie_colection(request):
    movies_list = Collection.objects.filter(coming_next=False).order_by('-date_added')
    latest_1 = movies_list[0:4]

    if request.method == 'GET':  # If the form is submitted
        queryset = []
        search_query = request.GET.get('search_box')
        if search_query is not None:
            queries = search_query.split(" ")
            for q in queries:
                movies_filter = Collection.objects.filter(
                    Q(title__icontains=q) | Q(description__icontains=q)).distinct()

                for movie in movies_filter:
                    queryset.append(movie)
                    movies_list = list(set(queryset))


    paginator = Paginator(movies_list,12)

    try:
        page = int(request.GET.get('page',1))
    except:
        page=1

    try:
        movies = paginator.page(page)

    except(EmptyPage,InvalidPage):
        movies=paginator.page(paginator.num_page)

    return render(request, "movies/colection.html", {'movies':movies,"latest_1":latest_1})

def movie_action(request):
    category = "Action"
    movies_list = Collection.objects.filter(Q(category1=category) | Q(category2=category) | Q(category3=category),coming_next=False).order_by('-date_added')
    paginator = Paginator(movies_list,12)
    try:
        page = int(request.GET.get('page',1))
    except:
        page=1

    try:
        movies = paginator.page(page)

    except(EmptyPage,InvalidPage):
        movies=paginator.page(paginator.num_page)

    return render(request, "movies/colection.html", {'movies':movies})

def movie_comedy(request):
    category="Comedy"
    movies_list = Collection.objects.filter(Q(category1=category) | Q(category2=category) | Q(category3=category),coming_next=False).order_by('-relese_date')
    paginator = Paginator(movies_list,12)
    try:
        page = int(request.GET.get('page',1))
    except:
        page=1

    try:
        movies = paginator.page(page)

    except(EmptyPage,InvalidPage):
        movies=paginator.page(paginator.num_page)

    return render(request, "movies/colection.html", {'movies':movies})


def movie_adventure(request):
    category="Adventure"
    movies_list = Collection.objects.filter(Q(category1=category) | Q(category2=category) | Q(category3=category),coming_next=False).order_by('-relese_date')
    paginator = Paginator(movies_list,12)
    try:
        page = int(request.GET.get('page',1))
    except:
        page=1

    try:
        movies = paginator.page(page)

    except(EmptyPage,InvalidPage):
        movies=paginator.page(paginator.num_page)

    return render(request, "movies/colection.html", {'movies':movies})

def movie_animation(request):
    category="Animation"
    movies_list = Collection.objects.filter(Q(category1=category) | Q(category2=category) | Q(category3=category),coming_next=False).order_by('-relese_date')
    paginator = Paginator(movies_list,12)
    try:
        page = int(request.GET.get('page',1))
    except:
        page=1

    try:
        movies = paginator.page(page)

    except(EmptyPage,InvalidPage):
        movies=paginator.page(paginator.num_page)

    return render(request, "movies/colection.html", {'movies':movies})

def movie_biographical(request):
    category="Biographical"
    movies_list = Collection.objects.filter(Q(category1=category) | Q(category2=category) | Q(category3=category),coming_next=False).order_by('-relese_date')
    paginator = Paginator(movies_list,12)
    try:
        page = int(request.GET.get('page',1))
    except:
        page=1

    try:
        movies = paginator.page(page)

    except(EmptyPage,InvalidPage):
        movies=paginator.page(paginator.num_page)

    return render(request, "movies/colection.html", {'movies':movies})


def movie_classic(request):
    category="Classic"
    movies_list = Collection.objects.filter(Q(category1=category) | Q(category2=category) | Q(category3=category),coming_next=False).order_by('-relese_date')
    paginator = Paginator(movies_list,12)
    try:
        page = int(request.GET.get('page',1))
    except:
        page=1

    try:
        movies = paginator.page(page)

    except(EmptyPage,InvalidPage):
        movies=paginator.page(paginator.num_page)

    return render(request, "movies/colection.html", {'movies':movies})

def movie_crime(request):
    category="Crime"
    movies_list = Collection.objects.filter(Q(category1=category) | Q(category2=category) | Q(category3=category),coming_next=False).order_by('-relese_date')
    paginator = Paginator(movies_list,12)
    try:
        page = int(request.GET.get('page',1))
    except:
        page=1

    try:
        movies = paginator.page(page)

    except(EmptyPage,InvalidPage):
        movies=paginator.page(paginator.num_page)

    return render(request, "movies/colection.html", {'movies':movies})




def movie_dramas(request):
    category="Drama"
    movies_list = Collection.objects.filter(Q(category1=category) | Q(category2=category) | Q(category3=category),coming_next=False).order_by('-relese_date')
    paginator = Paginator(movies_list,12)
    try:
        page = int(request.GET.get('page',1))
    except:
        page=1

    try:
        movies = paginator.page(page)

    except(EmptyPage,InvalidPage):
        movies=paginator.page(paginator.num_page)

    return render(request, "movies/colection.html", {'movies':movies})



def movie_family(request):
    category="Family"
    movies_list = Collection.objects.filter(Q(category1=category) | Q(category2=category) | Q(category3=category),coming_next=False).order_by('-relese_date')
    paginator = Paginator(movies_list,12)
    try:
        page = int(request.GET.get('page',1))
    except:
        page=1

    try:
        movies = paginator.page(page)

    except(EmptyPage,InvalidPage):
        movies=paginator.page(paginator.num_page)

    return render(request, "movies/colection.html", {'movies':movies})

def movie_fantasy(request):
    category="Fantasy"
    movies_list = Collection.objects.filter(Q(category1=category) | Q(category2=category) | Q(category3=category),coming_next=False).order_by('-relese_date')
    paginator = Paginator(movies_list,12)
    try:
        page = int(request.GET.get('page',1))
    except:
        page=1

    try:
        movies = paginator.page(page)

    except(EmptyPage,InvalidPage):
        movies=paginator.page(paginator.num_page)

    return render(request, "movies/colection.html", {'movies':movies})


def movie_romance(request):
    category="Romance"
    movies_list = Collection.objects.filter(Q(category1=category) | Q(category2=category) | Q(category3=category),coming_next=False).order_by('-relese_date')
    paginator = Paginator(movies_list,12)
    try:
        page = int(request.GET.get('page',1))
    except:
        page=1

    try:
        movies = paginator.page(page)

    except(EmptyPage,InvalidPage):
        movies=paginator.page(paginator.num_page)

    return render(request, "movies/colection.html", {'movies':movies})





def movie_scifi(request):
    category="Sci-Fi"
    movies_list = Collection.objects.filter(Q(category1=category) | Q(category2=category) | Q(category3=category),coming_next=False).order_by('-relese_date')
    paginator = Paginator(movies_list,12)
    try:
        page = int(request.GET.get('page',1))
    except:
        page=1

    try:
        movies = paginator.page(page)

    except(EmptyPage,InvalidPage):
        movies=paginator.page(paginator.num_page)

    return render(request, "movies/colection.html", {'movies':movies})


def movie_sports(request):
    category="Sport"
    movies_list = Collection.objects.filter(Q(category1=category) | Q(category2=category) | Q(category3=category),coming_next=False).order_by('-relese_date')
    paginator = Paginator(movies_list,12)
    try:
        page = int(request.GET.get('page',1))
    except:
        page=1

    try:
        movies = paginator.page(page)

    except(EmptyPage,InvalidPage):
        movies=paginator.page(paginator.num_page)

    return render(request, "movies/colection.html", {'movies':movies})



def movie_thrille(request):
    category="Thriller"
    movies_list = Collection.objects.filter(Q(category1=category) | Q(category2=category) | Q(category3=category),coming_next=False).order_by('-relese_date')
    paginator = Paginator(movies_list,12)
    try:
        page = int(request.GET.get('page',1))
    except:
        page=1

    try:
        movies = paginator.page(page)

    except(EmptyPage,InvalidPage):
        movies=paginator.page(paginator.num_page)

    return render(request, "movies/colection.html", {'movies':movies})



def coming_next(request):
    movies_list = Collection.objects.filter(coming_next=True,popular=False)
    paginator = Paginator(movies_list,12)
    try:
        page = int(request.GET.get('page',1))
    except:
        page=1

    try:
        movies = paginator.page(page)

    except(EmptyPage,InvalidPage):
        movies=paginator.page(paginator.num_page)

    return render(request, "movies/colection.html", {'movies':movies})



def popular(request):
    movies_list = Collection.objects.filter(popular=True,coming_next=False)
    paginator = Paginator(movies_list,12)
    try:
        page = int(request.GET.get('page',1))
    except:
        page=1

    try:
        movies = paginator.page(page)

    except(EmptyPage,InvalidPage):
        movies=paginator.page(paginator.num_page)

    return render(request, "movies/colection.html", {'movies':movies})


def detail(request, url):

    movie = Collection.objects.filter(url=url)
    # print(movie[0].category1)
    movies = Collection.objects.filter(
        Q(category1=movie[0].category1) | Q(category2=movie[0].category2),coming_next=False).exclude(title=movie[0].title)[0:12]
    return render(request, 'movies/detail.html', {'movie': movie,"movies":movies})




#
# def your_view(request):
#     movies=Collection.objects.all()
#
#
#     if request.method == 'GET': # If the form is submitted
#         queryset=[]
#         search_query = request.GET.get('search_box')
#         if search_query is not None:
#             queries = search_query.split(" ")
#             for q in queries:
#                 movies_filter = Collection.objects.filter(Q(title__icontains=q) | Q(description__icontains=q)).distinct()
#
#                 for movie in movies_filter:
#                     queryset.append(movie)
#                     movies = list(set(queryset))
#
#     return render(request, "movies/colection.html",{"movies":movies})







def contact(request):
    return render(request ,"contact.html")

def about(request):
    return render(request ,"about.html")

def inprogress(request):
    return render(request ,"inprogress.html")