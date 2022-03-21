from django import forms
from . import models
from django.contrib.auth import get_user_model

User = get_user_model()


class TicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = ["title", "description", "image"]
        labels = {"title": "Titre du livre", "description": "Résumé du livre"}


class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        exclude = ["ticket", "user", "time_created"]
        labels = {
            "rating": "Avis",
            "headline": "Titre",
            "body": "Corps",
        }
        widgets = {
            "rating": forms.RadioSelect(
                choices=[
                    (0, "1 - Mauvais"),
                    (1, "2 - Plutôt mauvais"),
                    (2, "3 - Mitigé"),
                    (3, "4 - Bon"),
                    (4, "5 - Très bon"),
                    (5, "6 - Génial"),
                ]
            )
        }
