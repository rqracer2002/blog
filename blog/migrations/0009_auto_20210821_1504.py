# Generated by Django 3.0.3 on 2021-08-21 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20210821_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='orderheader',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='mymodel', to='blog.OrderHeader'),
        ),
    ]
