# Generated by Django 3.0.3 on 2021-08-21 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20210821_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderheader',
            name='mymodel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mymodel', to='blog.MyModel'),
        ),
    ]