from django.conf.urls import include, url
from django.contrib import admin
from efill_app import views

urlpatterns = [
    url(r'^$', views.itr_form_view, name='itr_form_view'),
]
