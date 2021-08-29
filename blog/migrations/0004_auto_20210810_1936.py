# Generated by Django 3.0.3 on 2021-08-11 02:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_orderdetail_orderheader'),
    ]

    operations = [
        migrations.CreateModel(
            name='BinTransfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DecimalField(decimal_places=0, max_digits=9)),
                ('srctype', models.IntegerField()),
                ('doctype', models.IntegerField()),
                ('srcloc', models.CharField(max_length=6)),
                ('destloc', models.CharField(max_length=6)),
                ('srcbin', models.CharField(max_length=10)),
                ('destbin', models.CharField(max_length=10)),
                ('quantitytran', models.DecimalField(decimal_places=4, max_digits=19)),
                ('comment', models.CharField(max_length=250)),
                ('itemno', models.CharField(max_length=24)),
                ('itemdesc', models.CharField(max_length=60)),
            ],
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='orderheader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderdetail', to='blog.OrderHeader'),
        ),
    ]
