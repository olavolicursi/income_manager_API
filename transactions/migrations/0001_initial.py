# Generated by Django 5.0.2 on 2024-02-22 00:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_alter_account_user_id'),
        ('categories', '0002_category_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('emission_date', models.DateField()),
                ('payment_date', models.DateField(blank=True, null=True)),
                ('time', models.TimeField()),
                ('type', models.CharField(choices=[('C', 'C'), ('D', 'D')], max_length=1)),
                ('description', models.TextField(blank=True, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.account')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.category')),
            ],
        ),
    ]
