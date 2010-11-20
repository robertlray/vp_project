from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    short_description = models.CharField(max_length=255)
    copyright_field = models.CharField(max_length=255)
    id_number = models.IntegerField()
    def sorted_categories(self):
        return self.categories.order_by('id_number')
    def __unicode__(self):
        return self.title
class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    shot_date = models.DateField()
    video_name = models.FileField(upload_to='videos')
    thumbnail_name = models.FileField(upload_to='thumbnails')
    category = models.ForeignKey(Category,
                                 related_name='videos')
    def __unicode__(self):
        return self.title

