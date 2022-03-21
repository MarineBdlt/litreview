from django.conf import settings
from django.contrib.auth import login, get_user_model
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from authentication import models
from . import forms


def signup_page(request):
    form = forms.SignupForm()
    if request.method == "POST":
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, "signup.html", context={"form": form})


@login_required
def follow_users(request):
    form = forms.FollowUsersForm()
    if request.method == "POST":
        form = forms.FollowUsersForm(request.POST)
        if form.is_valid():
            followed_user = form.cleaned_data.get("username")
            user_f = get_user_model().objects.filter(username__exact=followed_user)
            if user_f:
                user = request.user
                models.UserFollow.objects.create(user=user, followed_user=user_f[0])
            return redirect("follow_users")
    following = models.UserFollow.objects.filter(user=request.user)
    followed_by = models.UserFollow.objects.filter(followed_user=request.user)
    context = {
        "form": form,
        "following": following,
        "followed_by": followed_by,
    }

    return render(request, "follow_users.html", context=context)


@login_required
def unfollow_users(request, user_id):
    user = get_user_model().objects.get(id__exact=user_id)
    following = models.UserFollow.objects.get(
        user__exact=request.user, followed_user__exact=user
    )

    if following:
        following.delete()

    return redirect("follow_users")
