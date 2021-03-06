# Generated by Django 3.2.7 on 2021-09-08 14:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Problem title')),
                ('category', models.IntegerField(choices=[(1, 'School'), (2, 'Car'), (3, 'Medicine'), (4, 'Psychology'), (5, 'Etc')], verbose_name='Problem category')),
                ('description', models.TextField(verbose_name='Problem full description')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
