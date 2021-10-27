from django.urls import path
from . import views

urlpatterns=[
    path ('zain',views.ntrends,name='zain'),
    path ('FXPRO',views.FXPRO,name='FXPRO'),
    path  ('nbh' ,views.nbh,name='nbh')

]
