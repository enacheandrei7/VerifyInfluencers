from django.urls import path
from .views import ClaimVerificationView, FetchTweetsView, FetchPodcastsView

urlpatterns = [
    path('claims/verify/', ClaimVerificationView.as_view()),
    path('influencers/<str:username>/tweets/', FetchTweetsView.as_view()),
    path('influencers/<str:name>/podcasts/', FetchPodcastsView.as_view()),
]
