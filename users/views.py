from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .form import UserRegister, UserUpdate, ProfileUpdate
from .models import Profile

# Create your views here.
def register(request):

    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            if form.cleaned_data.get("age") < 18:
                messages.error(request, "You are too young to register")
                form = UserRegister()
                return redirect("register")
            else:
                usrage = form.cleaned_data.get("age")
                form.save()
                username = form.cleaned_data.get("username")
                messages.success(
                    request, f"Account created successfully for {username}"
                )
                return redirect("login")
    else:
        form = UserRegister()
    return render(request, "users/register.html", {"form": form})


@login_required
def Profile(request):

    if request.method == "POST":

        u_form = UserUpdate(request.POST, instance=request.user)
        p_form = ProfileUpdate(
            request.POST, request.FILES, instance=request.user.profile
        )

        if u_form.is_valid() and p_form.is_valid():
            if p_form.cleaned_data.get("age") < 18:
                messages.error(request, "age cannot be below 18")
                p_form = ProfileUpdate()
                return redirect("profile")
            else:
                u_form.save()
                p_form.save()
                messages.success(request, "Profile Updated Successfully")
                return redirect("profile")
    else:
        u_form = UserUpdate(instance=request.user)
        p_form = ProfileUpdate(instance=request.user.profile)
    context = {
        "u_form": u_form,
        "p_form": p_form,
    }
    return render(request, "users/profile.html", context)
