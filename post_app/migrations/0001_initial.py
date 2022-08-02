# Generated by Django 4.0.6 on 2022-08-02 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Post text')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('author_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='user_app.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('author_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='user_app.customuser')),
                ('post_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='post_app.post')),
            ],
        ),
    ]
