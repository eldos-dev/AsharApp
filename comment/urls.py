from django.urls import path

from . import views

urlpatterns = [
    path("comment/create/", views.CommentCreateView.as_view()),
    path('comments/', views.CommentListView.as_view()),
    path('comment-detail/<int:pk>/', views.CommentDetailView.as_view()),
    path('comment/<int:pk>/', views.CommentUpdateDeleteView.as_view()),
]
