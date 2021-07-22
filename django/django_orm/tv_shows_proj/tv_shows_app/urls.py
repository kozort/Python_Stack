from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows', views.all_shows),
    path('shows/new', views.shows_new),
    path('shows/create', views.create),
    path('shows/<int:showID>', views.show_detail),
    path('shows/<int:showID>/edit', views.edit),
    path('shows/<int:showID>/update', views.update),
    path('shows/<int:showID>/destroy', views.delete)
    ]