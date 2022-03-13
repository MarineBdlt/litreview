from django.db import models
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class UserFollow(models.Model):
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="following",
    )
    followed_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="followed_by",
    )

    # __def__

    class Meta:
        unique_together = ("user", "followed_user")


#     contributors = models.ManyToManyField(
#         settings.AUTH_USER_MODEL,
#         through="BlogContributor",
#         related_name="contributions",
#     )

#     def _get_word_count(self):
#         return len(self.content.split(" "))

#     def save(self, *args, **kwargs):
#         self.word_count = self._get_word_count()
#         super().save(*args, **kwargs)


# class BlogContributor(models.Model):
#     contributor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
#     contribution = models.CharField(max_length=255, blank=True)

#     class Meta:
#         unique_together = ("contributor", "blog")
