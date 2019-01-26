# Generated by Django 2.1.5 on 2019-01-25 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(help_text='Book name', max_length=500)),
                ('book_url', models.URLField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conference_name', models.CharField(help_text='Book name', max_length=500)),
                ('conference_url', models.URLField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cover',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover_name', models.CharField(help_text='Cover name', max_length=500)),
                ('cover_url', models.URLField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publication_name', models.CharField(help_text='Publication name', max_length=500)),
                ('publication_url', models.URLField(null=True)),
            ],
        ),
    ]
