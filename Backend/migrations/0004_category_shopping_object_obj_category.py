# Generated by Django 5.2.1 on 2025-05-11 19:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0003_shopping_object_obj_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='shopping_object',
            name='Obj_Category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Backend.category'),
        ),
    ]
