# Generated by Django 4.2.4 on 2023-09-12 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_question_is_next_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='option',
            name='next_question',
        ),
        migrations.AddField(
            model_name='option',
            name='next_question',
            field=models.ManyToManyField(blank=True, null=True, related_name='linked_option', to='api.question'),
        ),
    ]
