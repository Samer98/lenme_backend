# Generated by Django 4.2.1 on 2023-06-02 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('installment', '0001_initial'),
        ('loan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='installment',
            name='loan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loan.loan'),
        ),
    ]
