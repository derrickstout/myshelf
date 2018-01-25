# Generated by Django 2.0.1 on 2018-01-20 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_book_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_type',
            field=models.CharField(choices=[('PRINT', 'Print Book'), ('AUDIO', 'Audiobook'), ('EBOOK', 'eBook')], default='PRINT', max_length=5),
        ),
        migrations.AddField(
            model_name='book',
            name='own',
            field=models.BooleanField(default=False),
        ),
    ]