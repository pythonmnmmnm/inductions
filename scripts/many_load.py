#/home/mnmmnm/django_projects/mysite/scripts/many_load.py
'''import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript unesco_load

from unesco.models import Category, States, Region, Iso, Site

def run():
    fhand = open('scripts/load.csv')
    reader = csv.reader(fhand)
    next(reader) # Advance past the header

    Category.objects.all().delete()
    States.objects.all().delete()
    Region.objects.all().delete()
    Iso.objects.all().delete()
    Site.objects.all().delete()

    for row in reader:
        print(row)

        y, created= Site.objects.get_or_create(year = row[3])

        try:
            y=int(row[3])
        except:
            y=None

        sta = States(name=row[8])
        sta.save()

        reg = Region(name=row[9])
        reg.save()

        cat = Category(name=row[7])
        cat.save()

        iso = Iso(name=row[10])
        iso.save()

        site = Site(name=row[0], year=y, area=row[6],description=row[1],justification=row[2],longitude=row[4],latitude=row[5])
        site.save()
'''
'''
import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Site, Category, States, Region, Iso

def run():
    fhand = open('scripts/load.csv')
    reader = csv.reader(fhand)
    next(reader) # Advance past the header

    Category.objects.all().delete()
    States.objects.all().delete()
    Region.objects.all().delete()
    Iso.objects.all().delete()
    Site.objects.all().delete()

    for row in reader:
        print(row)

        c , created = Category.objects.get_or_create(name=row[7])
        s , created = States.objects.get_or_create(name=row[8])
        r , created = Region.objects.get_or_create(name=row[9])
        i , created = Iso.objects.get_or_create(name=row[10])

        try:
            y=int(row[3])
        except:
            y=None

        try:
            z=float(row[4])
        except:
            z=None

        try:
            x=float(row[5])
        except:
            x=None
'''

'''
        try:
            w=float(row[6])
        except:
            w=None

        try:
            j=row[2]
        except:
            j=None

        #site = Site(name=row[0], description=row[1], justification=j,  year=y, longitude=z, latitude=x, area_hectares= w, category=c, state=s, region=r, iso=i)
        site = Site(name=row[0], description=row[1], justification=j,  year=y, longitude=z, latitude=x,area_hectares = w , category=c, states=s, regions=r, iso=i)
        site.save()'''


import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Site, Category, States, Region, Iso

def run():
    fhand = open('scripts/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader) # Advance past the header

    Category.objects.all().delete()
    States.objects.all().delete()
    Region.objects.all().delete()
    Iso.objects.all().delete()
    Site.objects.all().delete()

    for row in reader:
        print(row)

        c , created = Category.objects.get_or_create(name=row[7])
        s , created = States.objects.get_or_create(name=row[8])
        r , created = Region.objects.get_or_create(name=row[9])
        i , created = Iso.objects.get_or_create(name=row[10])


        try:
            y=int(row[3])
        except:
            y=None

        try:
            z=float(row[4])
        except:
            z=None

        try:
            x=float(row[5])
        except:
            x=None

        if row[6]=="":
            w=None
        else:
            w=float(row[6])

        #try:
           #w=float(row[6])
        #except:
          # w=None


        try:
            j=row[2]
        except:
            j=None

        site = Site(name=row[0], description=row[1], justification=j,  year=y, longitude=z, latitude=x, area_hectares= w, category=c, states=s, region=r, iso=i)
        #site = Site(name=row[0], description=row[1], justification=j,  year=y, longitude=z, latitude=x, area_hectares= w)
        site.save()