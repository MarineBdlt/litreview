from django import forms
from . import models
from django.contrib.auth import get_user_model

User = get_user_model()


class TicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = ["title", "description", "image"]


class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        exclude = ["ticket", "user", "time_created"]


# class DeleteTicketForm(forms.Form):
#     delete_blog = forms.BooleanField(widget=forms.HiddenInput, initial=True)


# class ReviewForm(forms.ModelForm):
#     change_blog = forms.BooleanField(widget=forms.HiddenInput, initial=True)

#     class Meta:
#         model = models.Blog
#         exclude = ["ticket", "user", "time_created"]


# class DeleteReviewForm(forms.Form):
#     delete_blog = forms.BooleanField(widget=forms.HiddenInput, initial=True)


# class FollowUsersForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ["follows"]
