from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='vspMovieHome'),
    path('<int:movie_id>', views.detail, name='vspMovieDetail'),
    path('<int:movie_id>/create', views.createreview, name='vspMovieCreateReview'),
    path('review/<int:review_id>', views.updatereview, name='vspMovieUpdateReview'),
    path('review/<int:review_id>/delete', views.deletereview, name='vspMovieDeleteReview'),
]