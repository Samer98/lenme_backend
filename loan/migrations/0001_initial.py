# Generated by Django 4.2.1 on 2023-06-02 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('investorOffer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.PositiveSmallIntegerField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('status', models.CharField(choices=[('Funded', 'Funded'), ('Delayed', 'Delayed'), ('Completed', 'Completed')], default='Pending', editable=False, max_length=10)),
                ('investor_offer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='investorOffer.investoroffer')),
            ],
        ),
    ]