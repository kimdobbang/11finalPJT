# Generated by Django 4.2.13 on 2024-05-20 02:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_fixed_dcls_month_alter_fixed_fixed_code_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fixed',
            old_name='sqcl_cnd',
            new_name='spcl_cnd',
        ),
        migrations.RenameField(
            model_name='installment',
            old_name='sqcl_cnd',
            new_name='spcl_cnd',
        ),
    ]