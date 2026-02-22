from django.urls import path
from .views import ChatHistoryListView
urlpatterns = [
    path("history/<str:room_name>/", ChatHistoryListView.as_view(), name='chat_history'),
]
