from django.urls import path

from reviews.views import ReviewView

urlpatterns = [
    path('', ReviewView.as_view()),
    path('/<int:review_id>', ReviewView.as_view()),
]
