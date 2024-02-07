import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django

django.setup()
from rango.models import Category, Page

def populate():

    python_pages = [
        {"title": "Official Python Tutorial", "url": "http://docs.python.org/2/tutorial/", "views": 32},
        {"title": "How to Think like a Computer Scientist", "url": "http://www.greenteapress.com/thinkpython/", "views": 16},
        {"title": "Learn Python in 10 Minutes", "url": "http://www.korokithakis.net/tutorials/python/", "views": 8}]

    django_pages = [
        {"title": "Official Django Tutorial",
         "url": "https://docs.djangoproject.com/en/1.9/intro/tutorial01/", "views": 32},
        {"title": "Django Rocks",
         "url": "http://www.djangorocks.com/", "views": 16},
        {"title": "How to Tango with Django",
         "url": "http://www.tangowithdjango.com/", "views": 8}]

    other_pages = [
        {"title": "Bottle", "url": "http://bottlepy.org/docs/dev/", "views": 32},
        {"title": "Flask", "url": "http://flask.pocoo.org", "views": 16}]

    cats = {"Python": {"pages": python_pages, "views": 128, "likes": 64},
            "Django": {"pages": django_pages, "views": 64, "likes": 32},
            "Other Frameworks": {"pages": other_pages, "views": 32, "likes": 16},
            "Pascal": {"pages": [], "views": 32, "likes": 16},
            "Perl": {"pages": [], "views": 32, "likes": 16},
            "Php": {"pages": [], "views": 32, "likes": 16},
            "Prolog": {"pages": [], "views": 32, "likes": 16},
            "Programming": {"pages": [], "views": 32, "likes": 16},
            }

    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for p in cat_data['pages']:
            # Ensure view count is greater than zero
            if p['views'] <= 0:
                p['views'] = 1  # Set view count to 1 if it's negative or zero
            add_page(c, p['title'], p['url'], p['views'])

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')

    return

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    
    return p

def add_cat(name):
    if name == "Python":
        c = Category.objects.get_or_create(name = name, views = 128, likes = 64)[0]
    elif name == "Django":
        c = Category.objects.get_or_create(name = name, views = 64, likes = 32)[0]
    else:
        c = Category.objects.get_or_create(name = name, views = 32, likes = 16)[0]
    
    c.save()
    return c

if __name__ == "__main__":
    print('Starting Rango population script...')
    populate()

