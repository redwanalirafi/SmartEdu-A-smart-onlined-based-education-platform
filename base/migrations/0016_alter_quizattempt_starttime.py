# Generated by Django 4.1.4 on 2022-12-24 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizattempt',
            name='starttime',
            field=models.FloatField(default=0.0),
        ),
    ]
