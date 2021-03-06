# Generated by Django 2.2.2 on 2019-07-02 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20190702_0459'),
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('book_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=40, verbose_name='Book Name')),
                ('borrowed_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Student')),
            ],
        ),
    ]
