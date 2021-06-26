from django.contrib import messages
from django.shortcuts import redirect, reverse
from movies import models as movie_models
from . import models as review_models
from . import forms


def create_review(request, pk):
  if request.method == "POST":
    form = forms.CreateReviewForm(request.POST)
    movie = movie_models.Movie.objects.get_or_none(pk=pk)
    if not movie:
        return redirect(reverse("core:home"))
    if form.is_valid():
        review = form.save()
        review.movie = movie
        review.created_by = request.user
        review.save()
        messages.success(request, "Movie reviewed")
        return redirect(reverse("movies:movie", kwargs={"pk": movie.pk}))


def delete_review(request, pk):
  review = review_models.Review.objects.get_or_none(pk=pk)
  r_movie = review.movie
  if request.user == review.created_by:
    review.delete()
  return redirect(reverse("movies:movie", kwargs={"pk": r_movie.pk}))  