#!/usr/bin/python

from vp_project.models import Video, Category
from django.shortcuts import get_object_or_404
import datetime

categories = {'firstvideo.txt': 18,
              'americanartists.txt': 17,
              'civilrights.txt': 16,
              'familyportraits.txt': 15,
              'neighborhood.txt': 14,
              'selfportraits.txt': 13,
              'portraitsforinstallation.txt': 12,
              'magritte.txt': 11,
              'berlinseries.txt': 10,
              'traditional_dance.txt': 9,
              'valentine.txt': 8,
              'newyork.txt': 7,
              'frenchartists.txt': 6,
              'sanfrancisco.txt': 5,
              'frenchwriters.txt': 4,
              'newengland.txt': 3,
              'fivecomposers.txt': 2,
              'digitallimmings.txt': 1
              }
for filename, category_id in categories.iteritems():
    current_category = get_object_or_404(Category, pk=category_id)
    fn = 'categoriesTXT/' + filename
    f = open(fn)
    z = f.readlines()
    for x in z:
        y = x.split(',')
        if len(y) >= 4:
            new_vid = Video()
            new_vid.title = y[0].strip('"')
            new_vid.datetime = y[1].strip('"')
            new_vid.description = ""
            new_vid.shotdate = datetime.datetime.now()
            new_vid.video_name = y[2].strip('"')
            new_vid.thumbnail_name = y[3].strip().strip('"')
            if len(y) == 5:
                new_vid.aspectratio = y[4].strip().strip('"')
            else:
                new_vid.aspectratio = "0"
            print "title = %s, datetime = %s, description = %s, shotdate = %s, videofname = %s, thumbnailfname = %s, aspectratio = %s" % (new_vid.title,new_vid.datetime,new_vid.description,new_vid.shotdate,new_vid.video_name,new_vid.thumbnail_name,new_vid.aspectratio)
            new_video_object.save()
    
