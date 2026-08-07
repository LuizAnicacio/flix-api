from django.urls import path
#from genres.views import GenreCreateListViews, GenreRetrieveUpdateDestroyView
from . import views


urlpatterns= [

    path('genres/', views.GenreCreateListViews.as_view(), name='genre-create-list'),
    path('genres/<int:pk>/', views.GenreRetrieveUpdateDestroyView.as_view(), name='genre-detail-view'),

]