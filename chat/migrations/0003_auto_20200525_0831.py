# Generated by Django 3.0.6 on 2020-05-25 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_auto_20200525_0728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='username1',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='chat',
            name='username2',
            field=models.CharField(max_length=100),
        ),
    ]