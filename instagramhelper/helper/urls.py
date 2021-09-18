from django.urls import path
from . import views
urlpatterns = [
    path('', views.HelperMainView.as_view(), name='helpermainview'),
]
