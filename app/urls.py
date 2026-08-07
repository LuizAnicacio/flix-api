from django.contrib import admin
from django.urls import path
from genres.views import GenreCreateListViews, GenreRetrieveUpdateDestroyView
from actors.views import ActorCreateListViews, ActorRetrieveUpdateDestroyView
from movies.views import MovieCreateListViews, MovieRetrieveUpdateDestroyView
from reviews.views import ReviewCreateListViews, ReviewRetrieveUpdateDestroyView



urlpatterns = [
    path('admin/', admin.site.urls),

    path('genres/', GenreCreateListViews.as_view(), name='genre-create-list'),
    path('genres/<int:pk>/', GenreRetrieveUpdateDestroyView.as_view(), name='genre-detail-view'),
    
    path('actors/', ActorCreateListViews.as_view(), name='actor-create-list'),
    path('actors/<int:pk>/', ActorRetrieveUpdateDestroyView.as_view(), name='actor-detail-view'),

    path('movies/', MovieCreateListViews.as_view(), name='Movie-create-list'),
    path('movies/<int:pk>/', MovieRetrieveUpdateDestroyView.as_view(), name='Movie-detail-view'),

     path('reviews/', ReviewCreateListViews.as_view(), name='Reviews-create-list'),
     path('reviews/<int:pk>/', ReviewRetrieveUpdateDestroyView.as_view(), name='Reviews-detail-view'),

]
