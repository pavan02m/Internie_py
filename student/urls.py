from django.urls import path
from student import views
app_name = 'student'

urlpatterns = [
    path("sign-up/", views.register_student, name='sign-up'),
]
