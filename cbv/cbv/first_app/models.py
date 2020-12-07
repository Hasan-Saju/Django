from django.db import models
from django.urls import reverse
# Create your models here.


class Musician(models.Model):
    # id=models.AutoField(primary_key=True)  by default eita thake
    # max_length,blank,null are some parameters
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name+" "+self.last_name

    # ei model er form submit korle kothay redirect hobe
    def get_absolute_url(self):
        # musician details url er jonno id lage
        # return reverse("first_app:index")  #its ok also
        return reverse("first_app:musician_details", kwargs={'pk': self.pk})


class Album(models.Model):
    artist = models.ForeignKey(
        Musician, on_delete=models.CASCADE, related_name='album_list')
    name = models.CharField(max_length=100)
    release_date = models.DateField()

    # <select>
    # <option value='1'>Worst</option>
    rating = (
        (1, "Worst"),
        (2, "Bad"),
        (3, "Not Bad"),
        (4, "Good"),
        (5, "Excellent"),
    )

    num_stars = models.IntegerField(choices=rating)

    # class Meta:
    #     db_table="album"
    # table name change

    def __str__(self):
        return self.name+", Rating: " + str(self.num_stars)
