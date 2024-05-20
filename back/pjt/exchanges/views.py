from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Exchange
from .serializers import ExchangeSerializer
# Create your views here.

api_key = settings.EX_API_KEY


@api_view(['GET'])
def save_exchange(request):
    url = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={api_key}&data=AP01'

    # API 데이터 조회
    response = requests.get(url).json()
    
    # 각 국가 환율을 순회하며 저장
    for dic in response:
        CUR_UNIT = dic['cur_unit']
        CUR_NM = dic['cur_nm']
        TTB = dic['ttb']
        TTS = dic['tts']
        DEAL_BAS_R = dic['deal_bas_r']

        save_data = {
            'CUR_UNIT': CUR_UNIT,
            'CUR_NM': CUR_NM,
            'TTB': TTB,
            'TTS': TTS,
            'DEAL_BAS_R': DEAL_BAS_R
        }

        serializer = ExchangeSerializer(data=save_data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

    return JsonResponse({'message' : 'save Exchange complete!'})


# [GET] 전체 정기예금 상품 조회
@api_view(['GET']) 
def get_exchange(request):
    if request.method == 'GET':
        exchange = Exchange.objects.all()
        serializer = ExchangeSerializer(exchange, many=True)
        return Response(serializer.data)
