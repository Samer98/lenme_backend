# Generated by Django 4.2 on 2023-04-15 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loanRequest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrower',
            name='type',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
