# Generated by Django 2.2.2 on 2019-07-02 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20190702_0908'),
    ]

    operations = [
        migrations.CreateModel(
            name='Magazine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mag_name', models.CharField(max_length=50, verbose_name='Magazine Name')),
            ],
        ),
    ]
