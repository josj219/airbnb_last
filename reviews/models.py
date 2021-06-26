from django.db import models
from core.models import CoreModel
from . import managers

class Review(CoreModel):

  """ Review Model """ 

  created_by = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="reviews")
  text = models.TextField()
  movie = models.ForeignKey("movies.Movie", on_delete=models.CASCADE, related_name="reviews", null=True, blank=True)
  book = models.ForeignKey("books.Book", on_delete=models.CASCADE, related_name="reviews", null=True, blank=True)
  rating = models.IntegerField()
  objects = managers.CustomModelManager()

  def __str__(self):
    return self.text
  
  def rating_average(self):
      avg = (
          self.accuracy
          + self.communication
          + self.cleanliness
          + self.location
          + self.check_in
          + self.value
      ) / 6
      return round(avg, 2)

  rating_average.short_description = "Avg."