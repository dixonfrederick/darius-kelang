# Generated by Django 4.1.3 on 2022-11-30 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authuser', '0002_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaksi',
            name='jenisTransaksi',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='transaksi',
            name='nominal',
            field=models.BigIntegerField(null=True),
        ),
    ]