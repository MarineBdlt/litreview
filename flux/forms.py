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

    #         ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)
    # rating = models.PositiveSmallIntegerField(
    #     validators=[MinValueValidator(0), MaxValueValidator(5)]
    # )
    # user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # time_created = models.DateTimeField(auto_now_add=True)
    # headline = models.CharField(max_length=128)
    # body = models.TextField(max_length=8192, blank=True)

    #         labels  = {
    #     'title':'Titulo',
    #     'publication_date':'Data de Publicação',
    #     'author':'Autor',
    #     'price':'Preço',
    #     'pages':'Número de Páginas',
    #     'book_type':'Formato'
    #     }
    # widgets = {
    #     'title': forms.TextInput(attrs={'class':'form-control'}),
    #     'publication_date': forms.TextInput(attrs={'class':'form-control'}),
    #     'author': forms.TextInput(attrs={'class':'form-control'}),
    #     'price': forms.TextInput(attrs={'class':'form-control'}),
    #     'pages': forms.TextInput(attrs={'class':'form-control'}),
    #     'book_type': forms.TextInput(attrs={'class':'form-control'}),
    # }


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
