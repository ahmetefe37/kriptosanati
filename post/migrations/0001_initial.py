# Generated by Django 4.0.6 on 2022-07-26 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=200, null=True)),
                ('info', models.TextField(blank=True, max_length=1000, null=True)),
                ('profil_picture', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('frequency', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('content', models.TextField(blank=True, max_length=5000, null=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], max_length=200, null=True)),
                ('category', models.CharField(choices=[('daily_news', 'Daily News'), ('sports', 'Sports'), ('health', 'Health'), ('crypto', 'Cryptocurrencies')], max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_updated', models.DateTimeField(auto_now_add=True, null=True)),
                ('image_post', models.ImageField(blank=True, null=True, upload_to='')),
                ('slug', models.SlugField(editable=False, max_length=210, unique=True)),
                ('view_counter', models.IntegerField(default=0, max_length=10)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='post.author')),
                ('tags', models.ManyToManyField(to='post.tag')),
            ],
            options={
                'ordering': ('-date_created',),
            },
        ),
    ]
