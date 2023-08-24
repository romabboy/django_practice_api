# Generated by Django 4.2.4 on 2023-08-23 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='women',
            name='cat_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='women.category'),
        ),
    ]
