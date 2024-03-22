from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Movie, Review
from .forms import ReviewForm

def home(request):
    #return HttpResponse('<h1>Welcome to Home Page</h1>')
    sSearchTerm = request.GET.get("vsiSearchMovie")
    if sSearchTerm:
        oMovies = Movie.objects.filter(title__icontains=sSearchTerm)
    else:
        oMovies = Movie.objects.all()
    return render(request, 'home.html', {'vsoSearchTerm' : sSearchTerm, 'vloMovies' : oMovies})

def about(request):
    return HttpResponse('<h1>Welcome to About Page</h1>')

def signup(request):
    sEmail = request.GET.get('vsiEmail')
    return render(request, 'signup.html', {'vsoEmail': sEmail})

def detail(request, movie_id):
    oMovie = get_object_or_404(Movie, pk=movie_id)
    lReviews = Review.objects.filter(movie = oMovie)
    return render(request, 'detail.html', {'vdoMovie': oMovie, 'vloReviews': lReviews})

@login_required
def createreview(request, movie_id):
    oMovie = get_object_or_404(Movie, pk=movie_id)
    if request.method == 'GET':
        return render(request, 'createreview.html', {
            'form': ReviewForm(),
            'vdoMovie': oMovie,
        })
    else:
        try:
            form = ReviewForm(request.POST)
            newReview = form.save(commit=False)
            newReview.user = request.user
            newReview.movie = oMovie
            newReview.save()
            return redirect('vspMovieDetail', newReview.movie.id)
        except ValueError: 
            return render(request, 'createreview.html', {
                'form': ReviewForm(),
                'vdoMovie': oMovie,
                'error': 'bad data passed in',
            })

@login_required        
def updatereview(request, review_id):
    oReview = get_object_or_404(Review, pk=review_id, user=request.user)
    if request.method == 'GET':
        oForm = ReviewForm(instance=oReview)
        return render(request, 'updatereview.html', {'vdoReview': oReview, 'form': oForm})
    else:
        try:
            oForm = ReviewForm(request.POST, instance=oReview)
            oForm.save()
            return redirect('vspMovieDetail', oReview.movie.id)
        except ValueError:
            return render(request, 'updatereview.html', {
                'vdoReview': oReview,
                'form': oForm,
                'error': 'Bad data in form',
            })
        
@login_required
def deletereview(request, review_id):
    oReview = get_object_or_404(Review, pk=review_id, user=request.user)
    oReview.delete()
    return redirect('vspMovieDetail', oReview.movie.id)
