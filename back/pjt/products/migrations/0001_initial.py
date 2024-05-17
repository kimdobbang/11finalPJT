# Generated by Django 4.2.13 on 2024-05-17 07:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fixed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fixed_code', models.CharField(max_length=50)),
                ('fixed_name', models.CharField(max_length=50)),
                ('dcls_month', models.CharField(max_length=50)),
                ('join_way', models.CharField(max_length=50)),
                ('mtrt_int', models.TextField()),
                ('sqcl_cnd', models.TextField()),
                ('join_deny', models.IntegerField()),
                ('join_member', models.TextField()),
                ('etc_note', models.TextField()),
                ('max_limit', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Installment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('installment_code', models.CharField(max_length=50)),
                ('installment_name', models.CharField(max_length=50)),
                ('dcls_month', models.CharField(max_length=50)),
                ('join_way', models.CharField(max_length=50)),
                ('mtrt_int', models.TextField()),
                ('sqcl_cnd', models.TextField()),
                ('join_deny', models.IntegerField()),
                ('join_member', models.TextField()),
                ('etc_note', models.TextField()),
                ('max_limit', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InstallmentOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intr_rate_type_nm', models.CharField(max_length=50)),
                ('rsrv_type_nm', models.CharField(max_length=50)),
                ('save_trm', models.CharField(max_length=50)),
                ('intr_rate', models.FloatField()),
                ('intr_rate2', models.FloatField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.installment')),
            ],
        ),
        migrations.CreateModel(
            name='FixedOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intr_rate_type_nm', models.CharField(max_length=50)),
                ('save_trm', models.CharField(max_length=50)),
                ('intr_rate', models.FloatField()),
                ('intr_rate2', models.FloatField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.fixed')),
            ],
        ),
    ]
