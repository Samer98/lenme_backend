# Generated by Django 4.2.1 on 2023-06-02 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0012_alter_loan_annual_interest_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='loan_amount',
            field=models.IntegerField(null=True),
        ),
    ]