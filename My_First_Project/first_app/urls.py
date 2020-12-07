from django.conf.urls import url
from django.urls import path
from first_app import views

app_name ="first_app"

urlpatterns = [
    path('index/',views.index,name='index'),
    path('',views.index,name='index'),
    #path('home/',views.home,name='home'),
    # just website/server r nam call korleo index page a jabe
    #path('',views.index,name='index'),
    path('form/',views.form,name='form'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),

]
