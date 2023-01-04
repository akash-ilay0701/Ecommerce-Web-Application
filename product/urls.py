from django.urls import path, include
from . import views


urlpatterns = [
   path('', views.home, name='home'),
   path('learnMore/<id>', views.learnMore, name='learnMore'),
   path('buyNow/<id>', views.buyNow, name='buyNow'),
   path('confirmBuy/<id>', views.confirmBuy, name='confirmBuy'),
   path('confirmed/',views.confirmed, name='confirmed')

]
