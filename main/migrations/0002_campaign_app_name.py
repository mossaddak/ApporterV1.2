# Generated by Django 4.2.1 on 2023-06-08 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='app_name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
