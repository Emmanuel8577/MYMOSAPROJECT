from django.contrib import admin
from django.urls import path,include
from home import views

admin.site.site_header=" THIS IS MOSA SET 2014 DB",
admin.site.site_title="Welcome to Mosa DB",
admin.site.index_title="You're Welcome Admin, How was your day today ?"


urlpatterns = [
   path('', views.home, name='home'),
   path('event', views.event, name='event'),
   path('Signin', views.Signin, name='Signin'),
   path('register', views.register, name='register'),
   path('blogs', views.blogs, name='blogs'),
   path('dues', views.dues, name='dues'),
   path('contact', views.contact, name='contact'),
   path('members', views.members, name='members')

]