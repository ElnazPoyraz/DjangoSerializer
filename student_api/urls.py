from django.urls import path
from .views import home, student_api, student_api_get_update_delete
urlpatterns = [
    path('home/', home),
    path('student/', student_api),
    path('student/<int:pk>/', student_api_get_update_delete)
]