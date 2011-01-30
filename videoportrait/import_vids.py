#!/usr/bin/python

from vp_project.models import Video, Category
from django.shortcuts import get_object_or_404
import datetime

categories = {'firstvideo.txt': 1,
              'americanartists.txt': 2,
              'civilrights.txt': 3,
              'familyportraits.txt': 4,
              'neighborhood.txt': 5,
              'selfportraits.txt': 6,
              'portraitsforinstallation.txt': 7,
              'magritte.txt': 8,
              'berlinseries.txt': 9,
              'traditional_dance.txt': 10,
              'valentine.txt': 11,
              'newyork.txt': 12,
              'frenchartists.txt': 13,
              'sanfrancisco.txt': 14,
              'frenchwriters.txt': 15,
              'newengland.txt': 16,
              'fivecomposers.txt': 17,
              'digitallimmings.txt': 18
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
            new_vid.title = y[0].strip('"').replace("&sbquo;",",").replace("&quot;",'"').replace("&eacute;","e")
            new_vid.datetime = y[1].strip('"').replace("&sbquo;",",")
            new_vid.description = ""
            new_vid.shot_date = datetime.datetime.now()
            new_vid.video_name = y[2].strip('"')
            new_vid.thumbnail_name = y[3].strip().strip('"')
            new_vid.category = current_category
            if len(y) == 5:
                new_vid.aspectratio = y[4].strip().strip('"')
            else:
                new_vid.aspectratio = "0"
            print "title = %s, datetime = %s, description = %s, shotdate = %s, videofname = %s, thumbnailfname = %s, category = %s, aspectratio = %s" % (new_vid.title,new_vid.datetime,new_vid.description,new_vid.shot_date,new_vid.video_name,new_vid.thumbnail_name,new_vid.category,new_vid.aspectratio)
            new_vid.save()
    
