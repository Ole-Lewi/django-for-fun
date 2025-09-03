from django.urls import path
from .views import predict_student_performance

urlpatterns = [
    path('predict/', predict_student_performance, name='predict_student_performance'),
]
