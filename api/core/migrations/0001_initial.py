# Generated by Django 4.1.1 on 2022-09-20 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('pseudo', models.CharField(max_length=45)),
                ('username', models.CharField(max_length=45, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('video_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45, unique=True)),
                ('duration', models.PositiveIntegerField()),
                ('source', models.FileField(upload_to='')),
                ('quality', models.CharField(choices=[('1080', '1080'), ('720', '720'), ('480', '480'), ('360', '360'), ('240', '240')], max_length=10)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.user')),
            ],
        ),
    ]
