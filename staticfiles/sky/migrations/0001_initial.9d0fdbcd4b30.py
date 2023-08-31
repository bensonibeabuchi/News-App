# Generated by Django 4.2.4 on 2023-08-29 11:33

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
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('content', models.TextField()),
                ('category', models.CharField(choices=[('Breaking', 'Breaking'), ('Entertainment', 'Entertainment'), ('Politics', 'Politics'), ('Sports', 'Sports'), ('Crypto', 'Crypto'), ('General', 'General'), ('Business', 'Business'), ('Science', 'Science'), ('Health', 'Health'), ('Technology', 'Technology')], default='General', max_length=50)),
                ('image', models.ImageField(upload_to='news_images')),
                ('other_image', models.ImageField(blank=True, null=True, upload_to='other_images')),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='published', max_length=10)),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'News',
                'ordering': ('-date_posted',),
            },
        ),
    ]
