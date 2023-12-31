# Generated by Django 4.2.1 on 2023-06-08 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0003_alter_loan_table'),
        ('installment', '0005_remove_installment_loan_installment_loan_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='installment',
            name='loan_id',
        ),
        migrations.AddField(
            model_name='installment',
            name='loan_request',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='loan.loan'),
            preserve_default=False,
        ),
    ]
