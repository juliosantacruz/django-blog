# Generated by Django 3.2.6 on 2021-08-18 22:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0002_author'),
        ('posts', '0005_alter_author_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='membership.author'),
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]