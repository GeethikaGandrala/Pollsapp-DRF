# Generated by Django 3.0.2 on 2020-01-30 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='question_text',
        ),
    ]
