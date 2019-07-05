# Generated by Django 2.2.2 on 2019-07-02 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_magazine'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_name', models.CharField(max_length=50, verbose_name='Article Name')),
                ('article_magazines', models.ManyToManyField(to='home.Magazine')),
            ],
        ),
    ]
