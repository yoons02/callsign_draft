# Generated by Django 4.0.3 on 2022-10-07 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_alter_post_end_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='flag_enddate',
            field=models.BooleanField(default=False),
        ),
    ]