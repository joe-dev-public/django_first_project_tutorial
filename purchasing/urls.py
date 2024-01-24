from django.urls import path

from . import views

urlpatterns = [
    # /purchasing
    path("", views.index, name="index"),
    # /purchasing/item/id
    path("item/<int:item_id>/", views.item, name="item"),
    # /purchasing/release/id
    path("release/<int:release_id>/", views.release, name="release"),
]
