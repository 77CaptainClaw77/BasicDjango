from django.contrib import admin
from django.urls import path,include
from home.views import home_page
from home.views import delete_query
from home.views import edit_query
from home.views import create_query
urlpatterns = [
    path('',home_page),
    path('delete/<id>',delete_query),
    path('edit/<id>',edit_query),
    path('create/',create_query),
]