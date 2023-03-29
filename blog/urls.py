from django.urls import path
from .views import AboutView, ArticleDetailView, HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/',AboutView.as_view(), name='about'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
]
