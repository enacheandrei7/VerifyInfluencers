from django.urls import path
from .views import ClaimVerificationView

urlpatterns = [
    path('api/influencers/<str:username>/content/', InfluencerContentView.as_view()),
    path('api/claims/extract/', ClaimExtractionView.as_view()),
    path('api/claims/verify/', ClaimVerificationView.as_view()),
    path('api/influencers/leaderboard/', LeaderboardView.as_view()),
]
