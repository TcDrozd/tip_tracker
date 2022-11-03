# Generated by Django 4.1.3 on 2022-11-02 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tip_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Cash', 'cash'), ('CC', 'credit card')], default='Cash', max_length=15)),
            ],
            options={
                'verbose_name_plural': 'tip types',
            },
        ),
        migrations.CreateModel(
            name='Tip_Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tip', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tiptype', to='tip_tracker_app.tip_type')),
            ],
            options={
                'verbose_name_plural': 'tip entries',
            },
        ),
    ]
