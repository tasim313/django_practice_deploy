from django.db import models
from django.urls import reverse
# Create your models here.


class musicians(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    instrument = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse('first:musician_details', kwargs={'pk': self.pk})


class album(models.Model):
    artist = models.ForeignKey(musicians, on_delete=models.CASCADE, related_name='album_list')
    name = models.CharField(max_length=50)
    release_date = models.DateTimeField()
    rating = (
        (1, 'worst'),
        (2, 'Bad'),
        (3, 'Not Bad'),
        (4, 'Good'),
        (5, 'Excellent'),
    )
    num_star = models.IntegerField(choices=rating)
