from django.urls import path
from .views import FetchTweetsAndGetVerifiedClaimsView, InfluencerListView

urlpatterns = [
    path('influencers/<str:name>/tweets/', FetchTweetsAndGetVerifiedClaimsView.as_view()),
    path('influencers/', InfluencerListView.as_view()),
]
