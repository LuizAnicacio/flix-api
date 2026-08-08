from django.urls import path
#from genres.views import GenreCreateListViews, GenreRetrieveUpdateDestroyView
from . import views

urlpatterns= [

    path('movies/', views.MovieCreateListViews.as_view(), name='movie-create-list'),
    path('movies/<int:pk>/', views.MovieRetrieveUpdateDestroyView.as_view(), name='movie-detail-view'),

]