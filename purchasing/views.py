# from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from datetime import datetime

from .models import Release

# Interesting to note that datetime.now() evaluates to the current time that
# the dev server (re)loads, rather than when the user loads the page ;¬)
content = "Hello world, " + str(datetime.now())


def index(request):
    last_fifty_releases = Release.objects.order_by("-added")[:50]
    template = loader.get_template("purchasing/index.html")
    context = {
        "old_content": content,
        "data_we_care_about": last_fifty_releases,
    }
    return HttpResponse(template.render(context, request))


def item(request, item_id):
    return HttpResponse("Viewing item: %s" % item_id)


def release(request, release_id):
    return HttpResponse("Viewing release: %s" % release_id)
