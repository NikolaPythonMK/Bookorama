# Generated by Django 4.2.2 on 2023-06-25 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_bookgenre_genre_delete_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='total_times_rated',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='book',
            name='rating',
            field=models.FloatField(),
        ),
    ]