# from django.shortcuts import render

from django.http import HttpResponse
from datetime import datetime

# Interesting to note that datetime.now() evaluates to the current time that
# the dev server (re)loads, rather than when the user loads the page ;¬)
content = "Hello world, " + str(datetime.now())


def index(request):
    return HttpResponse(content)


def item(request, item_id):
    return HttpResponse("Viewing item: %s" % item_id)


def release(request, release_id):
    return HttpResponse("Viewing release: %s" % release_id)
