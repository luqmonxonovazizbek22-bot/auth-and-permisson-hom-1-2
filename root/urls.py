from django.contrib import admin
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from app.views import LogoutView, RegisterView
from app.views import VerifyEmailView, ResendCodeView

schema_view = get_schema_view(
    openapi.Info(
        title="Radifus API",
        default_version='v1',
        description="0 dan boshlab",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    path("register/", RegisterView.as_view()),
    path("verify-email/", VerifyEmailView.as_view()),
    path("resend-code/", ResendCodeView.as_view()),
    path("login/", TokenObtainPairView.as_view()),
    path("refresh/", TokenRefreshView.as_view()),
    path("logout/", LogoutView.as_view()),
    # path("me/", MeView.as_view()),
]
