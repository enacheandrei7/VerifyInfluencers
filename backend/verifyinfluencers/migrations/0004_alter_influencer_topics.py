# Generated by Django 5.1.5 on 2025-02-04 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verifyinfluencers', '0003_alter_healthclaim_influencer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='influencer',
            name='topics',
            field=models.JSONField(blank=True, default=list),
        ),
    ]
