from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import get_user_model
from django.http import JsonResponse
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Fixed, FixedOption, Installment, InstallmentOption
from .serializers import FixedSerializer, FixedOptionsSerializer, InstallmentSerializer, InstallmentOptionsSerializer
from accounts.serializers import UserInfoSerializer

# Create your views here.

api_key = settings.API_KEY


@api_view(['GET'])
def save_fixed(request):
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'

    # API 데이터 조회
    response = requests.get(url).json()
    
    # 정기예금 상품 목록을 순회하며 저장
    for dic in response.get('result').get('baseList'):
        fixed_code = dic['fin_prdt_cd']
        fixed_name = dic['fin_prdt_nm']
        dcls_month = dic['dcls_month']
        join_way = dic['join_way']
        mtrt_int = dic['mtrt_int']
        spcl_cnd = dic['spcl_cnd']
        join_deny = dic['join_deny']
        join_member = dic['join_member']
        etc_note = dic['etc_note']
        max_limit = dic['max_limit']

        save_data = {
            'fixed_code': fixed_code,
            'fixed_name': fixed_name,
            'dcls_month': dcls_month,
            'join_way': join_way,
            'mtrt_int': mtrt_int,
            'spcl_cnd': spcl_cnd,
            'join_deny': join_deny,
            'join_member': join_member,
            'etc_note': etc_note,
            'max_limit': max_limit
        }

        serializer = FixedSerializer(data=save_data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

    # 정기예금 상품 옵션 목록을 순회하며 저장
    for dic in response.get('result').get('optionList'):
        fin_prdt_cd = dic['fin_prdt_cd']
        intr_rate_type_nm = dic['intr_rate_type_nm']
        save_trm = dic['save_trm']
        intr_rate = dic['intr_rate']
        intr_rate2 = dic['intr_rate2']

        save_data = {
            'intr_rate_type_nm': intr_rate_type_nm,
            'save_trm': save_trm,
            'intr_rate': intr_rate,
            'intr_rate2': intr_rate2,
        }

        # 옵션의 외래키는 데이터에서 가져올 수 없으므로 직접 입력한다.
        product = Fixed.objects.get(fixed_code=fin_prdt_cd)  # 참조하는 상품 조회
        serializer = FixedOptionsSerializer(data=save_data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save(product=product)    # 저장하는 과정에서 외래키를 입력

    return JsonResponse({'message' : 'save Fixed complete!'})



@api_view(['GET'])
def save_installment(request):
    url = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'

    # API 데이터 조회
    response = requests.get(url).json()
    
    # 적금 상품 목록을 순회하며 저장
    for dic in response.get('result').get('baseList'):
        installment_code = dic['fin_prdt_cd']
        installment_name = dic['fin_prdt_nm']
        dcls_month = dic['dcls_month']
        join_way = dic['join_way']
        mtrt_int = dic['mtrt_int']
        spcl_cnd = dic['spcl_cnd']
        join_deny = dic['join_deny']
        join_member = dic['join_member']
        etc_note = dic['etc_note']
        max_limit = dic['max_limit']

        save_data = {
            'installment_code': installment_code,
            'installment_name': installment_name,
            'dcls_month': dcls_month,
            'join_way': join_way,
            'mtrt_int': mtrt_int,
            'spcl_cnd': spcl_cnd,
            'join_deny': join_deny,
            'join_member': join_member,
            'etc_note': etc_note,
            'max_limit': max_limit
        }

        serializer = InstallmentSerializer(data=save_data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

    # 적금 상품 옵션 목록을 순회하며 저장
    for dic in response.get('result').get('optionList'):
        fin_prdt_cd = dic['fin_prdt_cd']
        intr_rate_type_nm = dic['intr_rate_type_nm']
        rsrv_type_nm = dic['rsrv_type_nm']
        save_trm = dic['save_trm']
        intr_rate = dic['intr_rate']
        intr_rate2 = dic['intr_rate2']

        save_data = {
            'intr_rate_type_nm': intr_rate_type_nm,
            'rsrv_type_nm': rsrv_type_nm,
            'save_trm': save_trm,
            'intr_rate': intr_rate,
            'intr_rate2': intr_rate2,
        }

        # 옵션의 외래키는 데이터에서 가져올 수 없으므로 직접 입력한다.
        product = Installment.objects.get(installment_code=fin_prdt_cd)  # 참조하는 상품 조회
        serializer = InstallmentOptionsSerializer(data=save_data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save(product=product)    # 저장하는 과정에서 외래키를 입력

    return JsonResponse({'message' : 'save Installment complete!'})


# [GET] 전체 정기예금 상품 조회
@api_view(['GET']) 
def get_fixed(request):
    if request.method == 'GET':
        fixed = Fixed.objects.all()
        serializer = FixedSerializer(fixed, many=True)
        return Response(serializer.data)
    
# [GET] 전체 정기예금 상품 옵션 조회
@api_view(['GET']) 
def get_fixedOption(request):
    if request.method == 'GET':
        fixedoption = FixedOption.objects.all()
        serializer = FixedOptionsSerializer(fixedoption, many=True)
        return Response(serializer.data)
    
# [GET] 전체 적금 상품 조회
@api_view(['GET']) 
def get_installment(request):
    if request.method == 'GET':
        installment = Installment.objects.all()
        serializer = InstallmentSerializer(installment, many=True)
        return Response(serializer.data)    

# [GET] 전체 적금 상품 옵션 조회
@api_view(['GET']) 
def get_installmentOption(request):
    if request.method == 'GET':
        installmentoption = InstallmentOption.objects.all()
        serializer = InstallmentOptionsSerializer(installmentoption, many=True)
        return Response(serializer.data)
    

# [POST] 정기예금 상품 가입
@api_view(['POST'])
def join_fixed(request, username, product_id):
    usermodel = get_user_model().objects.get(username=username)
    fixed = Fixed.objects.get(id=product_id)
    usermodel.fixed.add(fixed)
    serializer = UserInfoSerializer(usermodel)
    return Response(serializer.data, status=status.HTTP_200_OK)


# [POST] 적금 상품 가입
@api_view(['POST'])
def join_installment(request, username, product_id):
    usermodel = get_user_model().objects.get(username=username)
    installment = Installment.objects.get(id=product_id)
    usermodel.installment.add(installment)
    serializer = UserInfoSerializer(usermodel)
    return Response(serializer.data, status=status.HTTP_200_OK)
