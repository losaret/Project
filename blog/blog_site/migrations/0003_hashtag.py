# Generated by Django 2.2.5 on 2019-09-13 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_site', '0002_auto_20190913_1143'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('post', models.ManyToManyField(to='blog_site.blog_post')),
            ],
        ),
    ]
