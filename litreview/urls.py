"""litreview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

import authentication.views
import flux.views
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView,
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", flux.views.home, name="home"),
    path("signup/",
         authentication.views.signup_page,
         name="signup"),
    path(
        "",
        LoginView.as_view(
            template_name="login.html",
            redirect_authenticated_user=True,
        ),
        name="login",
    ),
    path(
        "logout/",
        LogoutView.as_view(template_name="login.html"),
        name="logout",
    ),
    path(
        "change-password/",
        PasswordChangeView.as_view(
            template_name="password_change.html",
        ),
        name="password-change",
    ),
    path(
        "change-password-done/",
        PasswordChangeDoneView.as_view(
            template_name="password_change_done.html"
        ),
        name="password_change_done",
    ),
    path("ticket-list",
         flux.views.ticket_list,
         name="ticket_list"),
    path(
        "ticket-detail/<int:ticket_id>",
        flux.views.ticket_detail,
        name="ticket_detail"
    ),
    path("write-ticket",
         flux.views.add_ticket,
         name="add_ticket"),
    path(
        "write-review/<int:ticket_id>",
        flux.views.add_review,
        name="add_review",
    ),
    path(
        "write-ticket-and-review/",
        flux.views.add_ticket_and_review,
        name="add_ticket_and_review",
    ),
    path("review-added/",
         flux.views.review_added,
         name="review_added"),
    path("follow-users/",
         authentication.views.follow_users,
         name="follow_users"),
    path(
        "unfollow-users/<int:user_id>",
        authentication.views.unfollow_users,
        name="unfollow_users",
    ),
    path(
        "profil/",
        flux.views.profil,
        name="profil",
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
