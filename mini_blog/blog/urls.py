from django.urls import path
from . import views

urlpatterns = [path('', views.PostView.as_view()),
               path('<int:pk>/', views.PostDetail.as_view()),
               path('review/<int:pk>/', views.AddComments.as_view(), name='add_comments'),
               path('<int:pk>/like/', views.AddLike.as_view(), name='add_like'),
               path('<int:pk>/dislike/', views.DisLike.as_view(), name='add_dislike')]