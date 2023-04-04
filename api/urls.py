from django.urls import path
from .views import CourseListView, CourseDetailView

urlpatterns = [
    
    path("cbv/api/", CourseListView.as_view() ),
    path("cbv/api/<int:pk>", CourseDetailView.as_view() ),
]
