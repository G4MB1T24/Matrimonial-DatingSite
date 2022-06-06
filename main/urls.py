from django.contrib import admin
from django.urls import path
from . import views
from .views import (
    WedPostListView,
    WedPostDetailView,
    WedPostCreateView,
    WedPostUpdateView,
    WedPostDeleteView,
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", WedPostListView.as_view(), name="home"),
    path("post/<int:pk>/", WedPostDetailView.as_view(), name="post-detail"),
    path("post/new/", WedPostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/update/", WedPostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", WedPostDeleteView.as_view(), name="post-delete"),
    path("find-profile", views.ListProfile, name="find-profiles"),
    path("future", views.UpcomingFeatures, name="future"),
]
