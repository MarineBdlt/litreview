# Generated by Django 4.0.2 on 2022-02-01 19:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ("flux", "0003_alter_review_rating"),
    ]

    operations = [
        migrations.AddField(
            model_name="review",
            name="time_created",
            field=models.DateTimeField(
                auto_now_add=True,
                default=datetime.datetime(2022, 2, 1, 19, 41, 41, 623743, tzinfo=utc),
            ),
            preserve_default=False,
        ),
    ]
