from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('trend_keywords/', views.TodayTrendsViews.as_view()),
    path('today_trends/', views.TrendsSearchViews.as_view()),
]
