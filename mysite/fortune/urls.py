from django.urls import path
from . import views

app_name = 'fortune'
urlpatterns = [
    # ex: /fortune/
    path('', views.index, name='index'),
    # ex: /fortune/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /fortune/verify/ -- redirects to view-fortune if approved
    path('verify/', views.verify, name='verify'),
    # ex: /fortune/view-fortune/
    path('view-fortune/', views.viewFortune, name='viewFortune'),
    # ex: /fortune/5/answer/
    path('<int:question_id>/answer/', views.answer, name='answer'),


]