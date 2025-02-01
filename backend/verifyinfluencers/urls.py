from django.urls import path
from .views import FetchTweetsView

urlpatterns = [
    path('influencers/<str:username>/tweets/', FetchTweetsView.as_view()),
]
