from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime
from django.template.defaultfilters import slugify

CATEGORY_CHOICES = (
    ('Comedy', 'Comedy'),
    ('Adventure', 'Adventure'),
    ('Sport', 'Sport'),
    ('Action', 'Action'),
    ('Animation', 'Animation'),
    ('Crime', 'Crime'),
    ('Drama', 'Drama'),
    ('Family', 'Family'),
    ('Fantasy', 'Fantasy'),
    ('Sports', 'Sports'),
    ('Thriller', 'Thriller'),
    ('Sci-Fi', 'Sci-Fi'),
    ('Biography', 'Biography'),
    ('Christmas', 'Christmas'),
    ('Romance', 'Romance'),
    ('Documentaries', 'Documentaries'),
    ('Classics', 'Classics'),
)
# Create your models here.
class Collection(models.Model):
    title = models.CharField(max_length=100,default="")
    date_added = models.DateTimeField(default=now)
    description = models.TextField(default="-")
    relese_date = models.PositiveIntegerField(validators=[MinValueValidator(1900), MaxValueValidator(datetime.now().year)],help_text="Use the following format: <YYYY>")
    image = models.ImageField(upload_to='')
    category1 = models.CharField(choices=CATEGORY_CHOICES, max_length=30,default="Adventure")
    category2 = models.CharField(choices=CATEGORY_CHOICES, max_length=30, default="Adventure")
    category3 = models.CharField(choices=CATEGORY_CHOICES, max_length=30, default="Adventure")
    imdb_rating=models.FloatField(default=0)
    rottentmatoes_rating=models.FloatField(default=0)
    popular = models.BooleanField(default=False)
    coming_next = models.BooleanField(default=False)
    url = models.SlugField(max_length=500, unique=True, blank=True)
    review = models.TextField(default="-")
    yt_link = models.URLField(max_length=200)
    imdb_link = models.URLField(max_length=200, default="https://www.youtube.com/v/v1gTI4BOPUw?version=3")
    budget = models.CharField(max_length=100,default="-")
    length = models.IntegerField(default=0)
    cum_gross =models.CharField(max_length=100,default="-")
    directors = models.CharField(max_length=100,default="")
    writers = models.CharField(max_length=100,default="")
    stars =  models.CharField(max_length=100,default="")
    other = models.TextField(default="-")

    def save(self, *args, **kwargs):
        self.url = slugify(self.title)
        super(Collection, self).save(*args, **kwargs)

    def __str__(self):
        return self.title




class Quiz(models.Model):
    quiz = models.CharField(default="-",max_length=1024)
    ans1 = models.CharField(default="-",max_length=1024)
    ans2 = models.CharField(default="-",max_length=1024)
    ans3 = models.CharField(default="-",max_length=1024)
    correct = models.CharField(default="-",max_length=1024)



class Comment(models.Model):
    comment_text = models.CharField(max_length=1024)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_on = models.DateTimeField(default=now)
    movie_id = models.IntegerField(default=0)

    def __str__(self):
        return self.comment_text
