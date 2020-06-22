# Generated by Django 3.0.7 on 2020-06-22 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=200)),
                ('original_title', models.CharField(max_length=250)),
                ('tagline', models.CharField(blank=True, max_length=250)),
                ('slug', models.SlugField(blank=True, max_length=200)),
                ('imdb_id', models.CharField(max_length=20)),
                ('release_date', models.DateField()),
                ('date_pub', models.DateTimeField(auto_now_add=True)),
                ('overview', models.TextField(blank=True)),
                ('poster_path', models.URLField(blank=True, null=True)),
                ('backdrop_path', models.URLField(blank=True, null=True)),
                ('vote_average', models.FloatField(blank=True, default=0, null=True)),
                ('vote_count', models.IntegerField(blank=True, default=0, null=True)),
                ('genres', models.ManyToManyField(blank=True, related_name='movies', to='movies.Genre')),
                ('keywords', models.ManyToManyField(blank=True, related_name='movies', to='movies.Keyword')),
            ],
        ),
    ]
