# Generated by Django 2.2.5 on 2019-10-03 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_site', '0003_hashtag'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_post',
            name='post_image',
            field=models.ImageField(null=True, upload_to='uploads/'),
        ),
    ]