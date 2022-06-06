from django.shortcuts import render
from .models import WedPost
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from users.models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.


# def index(request):
#     context = {"wedpost": WedPost.objects.all()}
#     return render(request, "main/index.html", context)


class WedPostListView(ListView):
    model = WedPost
    template_name = "main/index.html"
    context_object_name = "wedpost"
    ordering = ["-date_posted"]


class WedPostDetailView(DetailView):
    model = WedPost
    template_name = "main/post_detail.html"


class WedPostCreateView(LoginRequiredMixin, CreateView):
    model = WedPost
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class WedPostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = WedPost
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class WedPostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = WedPost
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def ListProfile(request):
    context = {"profile": Profile.objects.all()}
    return render(request, "main/profile_list.html", context)


def UpcomingFeatures(request):
    return render(request, "main/upcoming_features.html")
