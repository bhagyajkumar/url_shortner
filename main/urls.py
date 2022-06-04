from django.urls import path
from . import views
from django.views.generic import RedirectView


urlpatterns = [
    path('', views.home, name='home'),
    path('shorten_url/', views.shorten_url, name='shorten_url'),
    path('<str:key>', views.open_url, name='open_url'),
    path('favicon.ico',RedirectView.as_view(url='/static/images/favicon.ico')),
]