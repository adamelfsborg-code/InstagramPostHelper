from django.urls import path
from . import views
urlpatterns = [
    path('/', views.MainCoreView.as_view(), name='maincoreview'),
]
