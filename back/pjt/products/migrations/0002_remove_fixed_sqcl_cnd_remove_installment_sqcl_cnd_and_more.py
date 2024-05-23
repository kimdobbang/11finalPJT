# Generated by Django 4.2.13 on 2024-05-23 21:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fixed',
            name='sqcl_cnd',
        ),
        migrations.RemoveField(
            model_name='installment',
            name='sqcl_cnd',
        ),
        migrations.AddField(
            model_name='fixed',
            name='fin_co_no',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='fixed',
            name='fin_grp_no',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='fixed',
            name='kor_co_nm',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='fixed',
            name='spcl_cnd',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='installment',
            name='fin_co_no',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='installment',
            name='fin_grp_no',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='installment',
            name='kor_co_nm',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='installment',
            name='spcl_cnd',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='fixed',
            name='dcls_month',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='fixed',
            name='etc_note',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='fixed',
            name='fixed_code',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='fixed',
            name='fixed_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='fixed',
            name='join_deny',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='fixed',
            name='join_member',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='fixed',
            name='join_way',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='fixed',
            name='mtrt_int',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='fixedoption',
            name='intr_rate',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='fixedoption',
            name='intr_rate2',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='fixedoption',
            name='intr_rate_type_nm',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='fixedoption',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.fixed'),
        ),
        migrations.AlterField(
            model_name='fixedoption',
            name='save_trm',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='installment',
            name='dcls_month',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='installment',
            name='etc_note',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='installment',
            name='installment_code',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='installment',
            name='installment_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='installment',
            name='join_deny',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='installment',
            name='join_member',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='installment',
            name='join_way',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='installment',
            name='mtrt_int',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='installmentoption',
            name='intr_rate',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='installmentoption',
            name='intr_rate2',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='installmentoption',
            name='intr_rate_type_nm',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='installmentoption',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.installment'),
        ),
        migrations.AlterField(
            model_name='installmentoption',
            name='rsrv_type_nm',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='installmentoption',
            name='save_trm',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
