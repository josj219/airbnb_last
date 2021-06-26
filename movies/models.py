from django.urls import reverse
from django.db import models
from core.models import CoreModel
from . import managers

class Movie(CoreModel):
    """ Movie Model """

    title = models.CharField(max_length=120)
    year = models.IntegerField()
    cover_image = models.ImageField(null=True, blank=True)
    rating = models.IntegerField()
    category = models.ForeignKey(
        "categories.Category", on_delete=models.CASCADE, related_name="movies")
    director = models.ForeignKey(
        "people.Person", on_delete=models.CASCADE, related_name="movies")
    cast = models.ManyToManyField("people.Person")
    objects = managers.CustomModelManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("movies:movie", kwargs={"pk": self.pk})

    class Meta:
        ordering = ["-created_at"]

    def total_rating(self):
        all_reviews = self.reviews.all()
        ratings = 0
        if len(all_reviews) > 0:
            for review in all_reviews:
                ratings += review.rating
            return round(ratings / len(all_reviews), 2)
        return 0
