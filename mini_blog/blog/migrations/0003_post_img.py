# Generated by Django 4.1.6 on 2023-02-07 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_options_alter_post_author_alter_post_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(default='name.jpg', upload_to='image/%Y', verbose_name='Image'),
            preserve_default=False,
        ),
    ]
