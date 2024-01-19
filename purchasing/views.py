# from django.shortcuts import render

from django.http import HttpResponse
from datetime import datetime

# Interesting to note that datetime.now() evaluates to the current time that
# the dev server (re)loads, rather than when the user loads the page ;¬)
content = "Hello world, " + str(datetime.now())


def index(request):
    return HttpResponse(content)
