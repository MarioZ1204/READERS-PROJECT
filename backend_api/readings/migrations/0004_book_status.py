# Generated by Django 5.0.6 on 2024-05-20 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readings', '0003_book_delete_books'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='status',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]
