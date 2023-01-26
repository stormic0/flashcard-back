from django.urls import path
from . import views


app_name = 'words'

urlpatterns = [
    path('register/', views.CreateWordAPIView.as_view(), name='create-word'),
    path('retrieve/', views.RetrieveWordAPIView.as_view(), name='retrieve-word'),
    path('update/<int:pk>/', views.UpdateWordAPIView.as_view(), name='update-word'),
]
