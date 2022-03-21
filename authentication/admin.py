from django.contrib import admin
from authentication import models


class UserAdmin(admin.ModelAdmin):
    list_display = (
        "name",
    )


admin.site.register(models.UserFollow)
