# Generated by Django 4.2.8 on 2024-02-11 16:53

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('poster', models.ImageField(blank=True, upload_to='user_movies')),
                ('desc', models.TextField(blank=True)),
                ('release_date', models.DateField(default=django.utils.timezone.now)),
                ('actors', models.TextField(blank=True)),
                ('trailer_link', models.TextField(blank=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieapp.category')),
            ],
        ),
    ]