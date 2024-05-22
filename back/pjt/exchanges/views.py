from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Exchange
from .serializers import ExchangeSerializer
from decimal import Decimal, ROUND_DOWN

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
# Create your views here.

api_key = settings.EX_API_KEY


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def save_exchange(request):
    url = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={api_key}&data=AP01'

    # API 데이터 조회
    response = requests.get(url).json()
    
    # 각 국가 환율을 순회하며 저장
    for info in response:
        cur_unit = info.get('cur_unit')
        cur_nm = info.get('cur_nm')
        ttb = info.get('ttb')
        tts = info.get('tts')
        deal_bas_r = info.get('deal_bas_r')
        
        # 'JPY(100)'과 'IDR(100)'을 각각 'JPY'와 'IDR'로 변경
        if cur_unit == 'JPY(100)' or cur_unit == 'IDR(100)':
            cur_unit = cur_unit.split('(')[0]  # 'JPY(100)' -> 'JPY'
             # TTB, TTS, DEAL_BAS_R 값을 100으로 나누고 소수점 아래 두 자리까지 반올림
            ttb = (Decimal(ttb) / 100).quantize(Decimal('0.0001'), rounding=ROUND_DOWN) if ttb else None
            tts = (Decimal(tts) / 100).quantize(Decimal('0.0001'), rounding=ROUND_DOWN) if tts else None
            deal_bas_r = (Decimal(deal_bas_r) / 100).quantize(Decimal('0.0001'), rounding=ROUND_DOWN) if deal_bas_r else None

        save_data = {
            'CUR_UNIT': cur_unit,
            'CUR_NM': cur_nm,
            'TTB': str(ttb),
            'TTS': str(tts),
            'DEAL_BAS_R': str(deal_bas_r)
        }

        serializer = ExchangeSerializer(data=save_data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

    return JsonResponse({'message' : 'save Exchange complete!'})


# [GET] 전체 환율정보 조회
@permission_classes([IsAuthenticated])
@api_view(['GET']) 
def get_exchange(request):
    if request.method == 'GET':
        exchange = Exchange.objects.all()
        serializer = ExchangeSerializer(exchange, many=True)
        return Response(serializer.data)
