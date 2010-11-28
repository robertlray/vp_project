#!/usr/bin/python

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
    fn = 'categoriesTXT/' + filename
    f = open(fn)
    z = f.readlines()
    for x in z:
        y = x.split(',')
        if len(y) >= 4:
            title = y[0].strip('"')
            dateline = y[1].strip('"')
            videofilename = y[2].strip('"')
            thumbnailfilename = y[3].strip().strip('"')
            if len(y) == 5:
                aspectratio = y[4].strip().strip('"')
            else:
                aspectratio = ""
            print "title = %s, dateline = %s, videofilename = %s, thumbnailfilename = %s, aspectratio = %s" % (title,dateline,videofilename,thumbnailfilename,aspectratio)
    
