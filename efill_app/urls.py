from django.conf.urls import include, url
from django.contrib import admin
from efill_app import views

urlpatterns = [
    url(r'^form1/$', views.itr_form_view, name='itr_form_view'),
]
