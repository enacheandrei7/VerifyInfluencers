from django.urls import path
from .views import FetchTweetsAndGetVerifiedClaims

urlpatterns = [
    path('influencers/<str:name>/tweets/', FetchTweetsAndGetVerifiedClaims.as_view()),
]
