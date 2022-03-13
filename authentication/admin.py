from django.contrib import admin

from django.contrib import admin
from authentication import models


class UserAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = (
        "name",
    )  # liste les champs que nous voulons sur l'affichage de la liste


# admin.site.register(UserFollow, UserAdmin)
# Register your models here.


admin.site.register(models.UserFollow)
