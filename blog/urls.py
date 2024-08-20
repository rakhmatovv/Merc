from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name = 'home'), 
    path('cars/',cars,name='cars'),
    path('corporativClient/',corporativClient,name='corporativClient'),
    path('special/',special,name='special'),
    path('public/',public,name='public'),
    path('about/',about,name='about'),
    path('service/',service,name='service'),
    path('repair/',repair,name='repair'),
    path('spareparts/',spareparts,name='spareparts'),
    path('orderparts/',orderparts,name='orderparts'),
    path('garant/',garant,name='garant'),
    path('contact/',contact,name='contact'),
    path('carDetail/<str:pk>/',carDetail,name='carDetail'),
    path('zakaz/',zakaz,name='zakaz'),
    path('sign-in/',signIn,name='signin'),
    path('sign-up/',signUp,name='signup'),
]


