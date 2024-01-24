# from django.shortcuts import render

from django.http import HttpResponse
from datetime import datetime

from .models import Release

# Interesting to note that datetime.now() evaluates to the current time that
# the dev server (re)loads, rather than when the user loads the page ;¬)
content = "Hello world, " + str(datetime.now())


def index(request):
    last_fifty_releases = Release.objects.order_by("-added")[:50]
    output = "<br>".join([r.title for r in last_fifty_releases])
    return HttpResponse(content + "<br><br>Last 50 releases:<br><br>" + output)


def item(request, item_id):
    return HttpResponse("Viewing item: %s" % item_id)


def release(request, release_id):
    return HttpResponse("Viewing release: %s" % release_id)
