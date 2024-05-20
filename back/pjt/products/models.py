from django.db import models

# Create your models here.
class Fixed(models.Model):
    fixed_code = models.CharField(max_length=50, unique=True, null=True)    # 상품 코드
    fixed_name = models.CharField(max_length=50, null=True)    # 상품 이름
    dcls_month = models.CharField(max_length=50, null=True)    # 공시 제출월(YYYYMM)
    join_way = models.CharField(max_length=50, null=True)      # 가입 방법
    mtrt_int = models.TextField(null=True)                   # 만기 후 이자율
    spcl_cnd = models.TextField(null=True)                   # 우대 조건
    join_deny = models.IntegerField(null=True)               # 가입 제한
    join_member = models.TextField(null=True)                # 가입 대상
    etc_note = models.TextField(null=True)                   # 기타 유의사항
    max_limit = models.IntegerField(null=True)      # 최고한도
    
    
class FixedOption(models.Model):
    intr_rate_type_nm = models.CharField(max_length=50, null=True) # 저축 금리 유형명
    save_trm = models.CharField(max_length=50, null=True)          # 저축 기간 (개월)
    intr_rate = models.FloatField(null=True)                     # 저축 금리
    intr_rate2 = models.FloatField(null=True)                    # 최고 우대금리
    product = models.ForeignKey(Fixed, on_delete=models.CASCADE, null=True)    # 참조 상품


class Installment(models.Model):
    installment_code = models.CharField(max_length=50, unique=True, null=True)    # 상품 코드
    installment_name = models.CharField(max_length=50, null=True)    # 상품 이름
    dcls_month = models.CharField(max_length=50, null=True)    # 공시 제출월(YYYYMM)
    join_way = models.CharField(max_length=50, null=True)      # 가입 방법
    mtrt_int = models.TextField(null=True)                   # 만기 후 이자율
    spcl_cnd = models.TextField(null=True)                   # 우대 조건
    join_deny = models.IntegerField(null=True)               # 가입 제한
    join_member = models.TextField(null=True)                # 가입 대상
    etc_note = models.TextField(null=True)                   # 기타 유의사항
    max_limit = models.IntegerField(null=True)      # 최고한도
    
    
class InstallmentOption(models.Model):
    intr_rate_type_nm = models.CharField(max_length=50, null=True) # 저축 금리 유형명
    rsrv_type_nm = models.CharField(max_length=50, null=True)      # 적립 유형명
    save_trm = models.CharField(max_length=50, null=True)          # 저축 기간 (개월)
    intr_rate = models.FloatField(null=True)                     # 저축 금리
    intr_rate2 = models.FloatField(null=True)                    # 최고 우대금리
    product = models.ForeignKey(Installment, on_delete=models.CASCADE, null=True)    # 참조 상품
