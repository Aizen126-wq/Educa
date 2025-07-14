from django.urls import path
from .views import ListCourseView, CourseDetailView, CreateCourseView


urlpatterns = [
    path('list/', ListCourseView.as_view(), name='list_courses'),
    path('detail/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('create_course/', CreateCourseView.as_view(), name='create_course'),
]