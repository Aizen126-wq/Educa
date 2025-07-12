from django.urls import path
from .views import ListCourseView, CourseDetailView


urlpatterns = [
    path('list/', ListCourseView.as_view(), name='list_courses'),
    path('detail/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
]