# Generated by Django 3.2.25 on 2024-05-16 19:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('saite', '0002_parser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parser',
            name='group_tag',
        ),
        migrations.AddField(
            model_name='parser',
            name='group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='parsers', to='saite.telegramgroup'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parser',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='parsers', to='auth.user'),
            preserve_default=False,
        ),
    ]
