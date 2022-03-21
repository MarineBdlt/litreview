from django.contrib import admin
from flux.models import Ticket, Review


class TicketAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "user",
    )


admin.site.register(Ticket, TicketAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ("headline", "ticket", "user", "rating")


admin.site.register(Review, ReviewAdmin)
