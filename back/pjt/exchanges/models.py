from django.db import models

# Create your models here.
class Exchange(models.Model):
    CUR_UNIT = models.TextField()   # 통화코드
    CUR_NM = models.TextField()     # 국가/통화명
    TTB = models.TextField()        # 전신환(송금) 받을 때 = 원화로 바꿀 때
    TTS = models.TextField()        # 전신환(송금) 보낼 때 = 외화로 바꿀 때
    DEAL_BAS_R = models.TextField() # 매매 기준율
# null=True