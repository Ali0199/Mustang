# Generated by Django 3.1.4 on 2021-01-11 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chiqim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=50)),
                ('turi', models.CharField(max_length=50)),
                ('soni', models.IntegerField(max_length=4)),
                ('narxi', models.FloatField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Etiketika',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=50)),
                ('soni', models.IntegerField(max_length=4)),
                ('kg', models.FloatField(max_length=5)),
                ('narxi', models.FloatField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Idish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=50)),
                ('soni', models.IntegerField(max_length=4)),
                ('kg', models.FloatField(max_length=4)),
                ('narxi', models.FloatField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Karobka',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=50)),
                ('soni', models.IntegerField(max_length=5)),
                ('kg', models.FloatField(max_length=5)),
                ('narxi', models.FloatField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Kirim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=50)),
                ('turi', models.CharField(max_length=50)),
                ('soni', models.IntegerField(max_length=4)),
                ('narxi', models.FloatField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Kraska',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=50)),
                ('ksoni', models.IntegerField(max_length=5)),
                ('kg', models.FloatField(max_length=5)),
                ('soni', models.IntegerField(max_length=4)),
                ('narxi', models.FloatField(max_length=10)),
                ('etiketika', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admines.etiketika')),
                ('idish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admines.idish')),
                ('karobka', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admines.karobka')),
            ],
        ),
    ]