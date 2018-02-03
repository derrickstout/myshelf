# Generated by Django 2.0.1 on 2018-02-03 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_auto_20180121_2251'),
    ]

    operations = [
        migrations.CreateModel(
            name='Audiobook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True, null=True)),
                ('series', models.CharField(blank=True, max_length=150, null=True)),
                ('review', models.TextField(blank=True, null=True)),
                ('finished', models.BooleanField(default=False, verbose_name='Finished')),
                ('length', models.CharField(max_length=20)),
                ('authors', models.ManyToManyField(blank=True, to='books.Author')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True, null=True)),
                ('series', models.CharField(blank=True, max_length=150, null=True)),
                ('review', models.TextField(blank=True, null=True)),
                ('finished', models.BooleanField(default=False, verbose_name='Finished')),
                ('authors', models.ManyToManyField(blank=True, to='books.Author')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Narrator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('narrator', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='PrintBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True, null=True)),
                ('series', models.CharField(blank=True, max_length=150, null=True)),
                ('review', models.TextField(blank=True, null=True)),
                ('finished', models.BooleanField(default=False, verbose_name='Finished')),
                ('authors', models.ManyToManyField(blank=True, to='books.Author')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='book',
            name='authors',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.AddField(
            model_name='audiobook',
            name='narrator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='books.Narrator'),
        ),
    ]
