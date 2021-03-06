# Generated by Django 3.0rc1 on 2019-12-03 07:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TrelloBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('date_created', models.DateField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TrelloList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('date_created', models.DateField(default=django.utils.timezone.now)),
                ('trello_board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.TrelloBoard')),
            ],
        ),
        migrations.CreateModel(
            name='TrelloCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('content', models.CharField(max_length=200)),
                ('date_created', models.DateField(default=django.utils.timezone.now)),
                ('trello_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.TrelloList')),
            ],
        ),
    ]
