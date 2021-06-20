# Generated by Django 3.2.4 on 2021-06-20 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MemberSite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('server', models.URLField()),
                ('website', models.URLField(blank=True, null=True)),
                ('discord', models.URLField(blank=True, null=True)),
                ('description', models.TextField()),
            ],
        ),
    ]
