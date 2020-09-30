from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
app_name = 'fortune'
urlpatterns = [
    # ex: /fortune/
    path('', views.index, name='index'),
    # ex: /fortune/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /fortune/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /fortune/5/answer/
    path('<int:question_id>/answer/', views.answer, name='answer'),
]