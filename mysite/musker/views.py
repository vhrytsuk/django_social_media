from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from .models import Profile, Meep
from .forms import MeepForm, SignUpForm, UpdateForm, ProfilePicForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


def home(request):
    if request.user.is_authenticated:
        form = MeepForm(request.POST or None, request.FILES or None)

        if request.method == "POST":
            if form.is_valid():
                meep = form.save(commit=False)
                meep.user = request.user
                meep.save()
                messages.success(request, "Meep Created")

                return redirect("home")
            else:
                messages.error(request, "Error creating Meep")

        meeps = Meep.objects.all().order_by("-created_at")

        return render(request, "home.html", {"meeps": meeps, "form": form})
    else:
        meeps = Meep.objects.all().order_by("-created_at")

        return render(request, "home.html", {"meeps": meeps})


def profile_list(request):
    if request.user.is_authenticated:
        profiles = Profile.objects.exclude(user=request.user)
        return render(request, "profile_list.html", {"profiles": profiles})
    else:
        messages.success(request, "Please login to view profiles")
        return redirect("home")


def follow(request, pk):
    if request.user.is_authenticated:
        # Get profile to unfollow
        profile = Profile.objects.get(user_id=pk)
        # Follow user
        request.user.profile.follows.add(profile)

        request.user.profile.save()

        messages.success(
            request, f"You have successfully followed {profile.user.username}"
        )
        return redirect(request.META.get("HTTP_REFERER"))

    else:
        messages.success(request, "Please login to unfollow")
        return redirect("home")


def unfollow(request, pk):
    if request.user.is_authenticated:
        # Get profile to unfollow
        profile = Profile.objects.get(user_id=pk)
        # Unfollow user
        request.user.profile.follows.remove(profile)

        request.user.profile.save()

        messages.success(
            request, f"You have successfully unfollowed {profile.user.username}"
        )
        return redirect(request.META.get("HTTP_REFERER"))

    else:
        messages.success(request, "Please login to unfollow")
        return redirect("home")


def profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        meeps = Meep.objects.filter(user=profile.user).order_by("-created_at")

        # Post Form logic
        if request.method == "POST":
            # Get current user
            current_user_profile = request.user.profile
            # Get form data
            action = request.POST["follow"]
            # Decide to follow or unfollow
            if action == "unfollow":
                current_user_profile.follows.remove(profile)
            else:
                current_user_profile.follows.add(profile)

            # Save the profile
            current_user_profile.save()

        return render(request, "profile.html", {"profile": profile, "meeps": meeps})
    else:
        messages.success(request, "Please login to view profile")
        return redirect("home")


def followers(request, pk):
    if request.user.is_authenticated:
        if request.user.id == pk:
            profiles = Profile.objects.get(user_id=pk)

            return render(request, "followers.html", {"profiles": profiles})
        else:
            messages.error(request, "That's not your profile")
            return redirect("home")
    else:
        messages.success(request, "Please login to view profiles")
        return redirect("home")


def follows(request, pk):
    if request.user.is_authenticated:
        if request.user.id == pk:
            profiles = Profile.objects.get(user_id=pk)

            return render(request, "follows.html", {"profiles": profiles})
        else:
            messages.error(request, "That's not your profile")
            return redirect("home")
    else:
        messages.success(request, "Please login to view profiles")
        return redirect("home")


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        print(request.POST)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful")

            return redirect("home")
        else:
            messages.error(request, "Login unsuccessful")

            return redirect("home")
    else:
        return render(request, "login.html", {})


def logout_user(request):
    logout(request)
    messages.success(request, "Logout successful")

    return redirect("home")


def register_user(request):
    form = SignUpForm()

    if request.user.is_authenticated:
        return redirect("home")
    else:
        if request.method == "POST":
            form = SignUpForm(request.POST)

            if form.is_valid():
                form.save()
                username = form.cleaned_data["username"]
                password = form.cleaned_data["password1"]
                # first_name = form.cleaned_data["first_name"]
                # last_name = form.cleaned_data["last_name"]
                # email = form.cleaned_data["email"]

                # Login
                user = authenticate(username=username, password=password)
                login(request, user)

                messages.success(request, "You have succesfully registered!")
                return redirect("home")
        return render(request, "register.html", {"form": form})


def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        profile_user = Profile.objects.get(user_id=request.user.id)

        # Get forms
        user_form = SignUpForm(
            request.POST or None, request.FILES or None, instance=current_user
        )
        profile_form = ProfilePicForm(
            request.POST or None, request.FILES or None, instance=profile_user
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            login(request, current_user)

            messages.success(request, "Your password has been updated!")
            return redirect("home")

        return render(
            request,
            "update_user.html",
            {"user_form": user_form, "profile_form": profile_form},
        )

    else:
        return redirect("home")


def meep_like(request, pk):
    if request.user.is_authenticated:
        meep = get_object_or_404(Meep, id=pk)

        if meep.likes.filter(id=request.user.id):
            meep.likes.remove(request.user)
        else:
            meep.likes.add(request.user)

        return redirect(request.META.get("HTTP_REFERER"))
    else:
        messages.error(request, "You must bee login to like a meep")
        return redirect("home")


def meep_show(request, pk):
    if request.user.is_authenticated:
        meep = get_object_or_404(Meep, id=pk)

        if meep:
            return render(request, "show_meep.html", {"meep": meep})
        else:
            messages.error(request, "Meep dosen't exist")
            return redirect("home")

    else:
        messages.error(request, "You must bee login to view a meep")
        return redirect("home")


def delete_meep(request, pk):
    if request.user.is_authenticated:
        meep = get_object_or_404(Meep, id=pk)

        if meep.user.username == request.user.username:
            meep.delete()
            messages.success(request, "Meep deleted")

            return redirect(request.META.get("HTTP_REFERER"))
        else:
            messages.error(request, "You can't delete this meep")
            return redirect("home")
    else:
        messages.error(request, "You must bee login to delete a meep")
        return redirect("home")


def edit_meep(request, pk):
    if not request.user.is_authenticated:
        messages.error(request, "You must be logged in to edit a meep")
        return redirect("home")

    meep = get_object_or_404(Meep, id=pk)

    if meep.user != request.user:
        messages.error(request, "You can't edit this meep")
        return redirect("home")

    meep_form = MeepForm(request.POST or None, request.FILES or None, instance=meep)

    if request.method == "POST":
        if meep_form.is_valid():
            meep = meep_form.save()
            meep.user = request.user

            messages.success(request, "Meep updated")

            return redirect(reverse("profile", kwargs={"pk": request.user.id}))
    else:
        return render(
            request,
            "edit_meep.html",
            {"meep_form": meep_form},
        )


def search(request):
    if request.method == "POST":
        search = request.POST["search"]

        # Search meeps in database
        searched_meeps = Meep.objects.filter(body__contains=search).order_by(
            "-created_at"
        )

        return render(
            request, "search.html", {"search": search, "searched_meeps": searched_meeps}
        )

    return render(request, "search.html", {})


def search_users(request):
    if request.method == "POST":
        search = request.POST["search"]

        # Search users in database
        searched_users = User.objects.filter(username__contains=search)

        return render(
            request,
            "search_users.html",
            {"search": search, "searched_users": searched_users},
        )

    return render(request, "search_users.html", {})
