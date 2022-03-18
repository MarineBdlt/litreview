from django.conf import settings
from django.contrib.auth import login, get_user_model
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from authentication import models
from . import forms


def signup_page(request):
    form = forms.SignupForm()
    if request.method == "POST":
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, "signup.html", context={"form": form})


@login_required
def follow_users(request):
    print("je suis dans la view")
    form = forms.FollowUsersForm()
    if request.method == "POST":
        print("je suis dans le post")
        form = forms.FollowUsersForm(request.POST)
        if form.is_valid():
            followed_user = form.cleaned_data.get("username")
            print("user cherché", followed_user)
            user_f = get_user_model().objects.filter(username__exact=followed_user)
            print("user trouvé en bdd", user_f)
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
    print("USER", user)
    following = models.UserFollow.objects.get(
        user__exact=request.user, followed_user__exact=user
    )

    if following:
        following.delete()

    return redirect("follow_users")
