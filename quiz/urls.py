from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("quiz/", views.quiz_page, name="quiz"),
    path("submit/", views.submit_quiz, name="submit"),
]
