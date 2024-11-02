from django.urls import path
from .views import create_admin, create_moderator_author, signup_view, login_view
urlpatterns = [
    path("admin/", create_admin),
    path("signup/", signup_view),
    path("change-role/<int:id>/", create_moderator_author),
    path("login/", login_view),
    ]