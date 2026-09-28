from django.urls import path
from . import views


urlpatterns = [
    path('reviews/', views.ReviewCreateListViews.as_view(), name='Reviews-create-list'),
    path('reviews/<int:pk>/', views.ReviewRetrieveUpdateDestroyView.as_view(), name='Reviews-detail-view'),
]
