# Generated by Django 3.0.1 on 2019-12-28 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='color_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='composition_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='size_id',
            field=models.IntegerField(),
        ),
    ]