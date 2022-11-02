""" Defines URL patterns for tip_tracker_app """

from django.urls import include, re_path

from . import views

urlpatterns = [
    # Homepage
    re_path(r'^$', views.index, name='index'),

    # Show your recent logs
    re_path(r'^entries/$', views.entries, name='entries'),

    # Page for just CC tips or Cash tips
    re_path(r'^types/$', views.types, name='types'),

    # Page for individual type
    re_path(r'^type/(?P<type_id>\d+)/$', views.type, name='type'),

    # Page for adding a new entry
    re_path(r'^new_entry/$', views.new_entry, name='new_entry'),

    # Page to edit a previous entry
    re_path(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]