from django.urls import path, include, re_path
from rest_framework import routers
from .views import (
    ToggleUserActivation,
    VerifyToken,
    CustomTokenObtainPairView,
    UserViewSet,
    UserSpecificView,
    ResetPassword,
)

router = routers.DefaultRouter()
router.register(r"users", UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    re_path(r"^users/(?P<id>\w+)/$", UserSpecificView.as_view()),
    path("api/token/", CustomTokenObtainPairView.as_view()),
    path("api/verify-token/", VerifyToken.as_view()),
    path("api/reset-password/", ResetPassword.as_view()),
    path(
        "api/toggle-activation/",
        ToggleUserActivation.as_view(),
        name="toggle-activation",
    ),
]