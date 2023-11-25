# Generated by Django 4.2.5 on 2023-10-04 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SpaceTech', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.URLField()),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ['title'],
                'indexes': [models.Index(fields=['title'], name='SpaceTech_c_title_4e6e5b_idx')],
            },
        ),
    ]
