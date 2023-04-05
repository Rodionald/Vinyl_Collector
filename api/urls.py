from django.urls import path
from api.views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('vinyls/', VinylListView.as_view()),
    path('vinyls/<int:pk>', VinylDetailsView.as_view()),
    path('users/', UserList.as_view()),
    path('register/', RegisterView.as_view(), name='sign_up'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
