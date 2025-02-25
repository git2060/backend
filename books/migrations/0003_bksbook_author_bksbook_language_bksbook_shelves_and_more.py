# Generated by Django 5.1.6 on 2025-02-21 19:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_remove_bksbkbookshelves_bookshelf_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bksbook',
            name='author',
            field=models.ManyToManyField(related_name='books', to='books.bksauthor'),
        ),
        migrations.AddField(
            model_name='bksbook',
            name='language',
            field=models.ManyToManyField(related_name='books', to='books.bkslanguage'),
        ),
        migrations.AddField(
            model_name='bksbook',
            name='shelves',
            field=models.ManyToManyField(related_name='books', to='books.bksbookshelf'),
        ),
        migrations.AddField(
            model_name='bksbook',
            name='subject',
            field=models.ManyToManyField(related_name='books', to='books.bkssubject'),
        ),
        migrations.RemoveField(
            model_name='bksbkauthors',
            name='book',
        ),
        migrations.RemoveField(
            model_name='bksbkbookshelves',
            name='book',
        ),
        migrations.RemoveField(
            model_name='bksbklanguages',
            name='book',
        ),
        migrations.RemoveField(
            model_name='bksbksubjects',
            name='book',
        ),
        migrations.AlterField(
            model_name='bksformat',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='format', to='books.bksbook'),
        ),
        migrations.AddField(
            model_name='bksbkauthors',
            name='book',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='book_authors', to='books.bksbook'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bksbkbookshelves',
            name='book',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='shelve', to='books.bksbook'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bksbklanguages',
            name='book',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='laguage', to='books.bksbook'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bksbksubjects',
            name='book',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='books.bksbook'),
            preserve_default=False,
        ),
    ]
