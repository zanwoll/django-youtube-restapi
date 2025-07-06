from django.urls import path
from .views import VideoList, VideoDetail

# api/v1/videos - VideoList
# api/v1/videos/{video_id} - VideoDetail
urlpatterns = [
    path('', VideoList.as_view(), name='video-list'),
    path('<int:pk>', VideoDetail.as_view(), name='video-detail'),
]