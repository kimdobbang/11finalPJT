from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
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

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# Create your views here.

api_key = settings.API_KEY

# ----------- 저장 -----------

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def save_fixed(request):
    ## (1) 1금융권 상품 목록 저장
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'

    # API 데이터 조회하여 request 객체 생성
    response = requests.get(url).json()
    
    # Fixed 정기예금 상품 목록을 순회하며 저장
    for dic in response.get('result').get('baseList'):
        fin_co_no = dic['fin_co_no']
        kor_co_nm = dic['kor_co_nm']
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
            'fin_grp_no': 1,
            'fin_co_no': fin_co_no,
            'kor_co_nm': kor_co_nm,
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
        
        # 중복 저장 방지
        if Fixed.objects.filter(kor_co_nm=kor_co_nm, fixed_code=fixed_code).exists():
            return JsonResponse({'message' : 'Data already stored'})
            
        # 직렬화 및 유효성검사 후 저장
        serializer = FixedSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

    # FixedOption 정기예금 상품 옵션 목록을 순회하며 저장
    for dic in response.get('result').get('optionList'):
        fin_prdt_cd = dic['fin_prdt_cd']
        fin_co_no = dic['fin_co_no']
        intr_rate_type_nm = dic['intr_rate_type_nm']
        save_trm = dic['save_trm']
        intr_rate = dic['intr_rate']
        intr_rate2 = dic['intr_rate2']

        save_data = {
            'intr_rate_type_nm': intr_rate_type_nm,
            'save_trm': save_trm,
            'intr_rate': intr_rate,
            'intr_rate2': intr_rate2
        }
        # 옵션의 외래키는 api response에서 가져올 수 없으므로 직접 입력한다.
        product = Fixed.objects.get(fixed_code=fin_prdt_cd, fin_co_no=fin_co_no )  # 외래키가 참조하는 상품 조회
        serializer = FixedOptionsSerializer(data=save_data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save(product=product)    # 저장하는 과정에서 외래키를 입력


    ## (2) 저축은행 상품 목록 저장
    for num in range(1, 5):
        url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=030300&pageNo={num}'

        # API 데이터 조회하여 request 객체 생성
        response = requests.get(url).json()
        
        # Fixed 정기예금 상품 목록을 순회하며 저장
        for dic in response.get('result').get('baseList'):
            fin_co_no = dic['fin_co_no']
            kor_co_nm = dic['kor_co_nm']
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
                'fin_grp_no': 2,
                'fin_co_no': fin_co_no,
                'kor_co_nm': kor_co_nm,
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
            
            # 중복 저장 방지
            if Fixed.objects.filter(kor_co_nm=kor_co_nm, fixed_code=fixed_code).exists():
                return JsonResponse({'message' : 'Data already stored'})
                
            # 직렬화 및 유효성검사 후 저장
            serializer = FixedSerializer(data=save_data)

            if serializer.is_valid(raise_exception=True):
                serializer.save()

        # FixedOption 정기예금 상품 옵션 목록을 순회하며 저장
        for dic in response.get('result').get('optionList'):
            fin_prdt_cd = dic['fin_prdt_cd']
            fin_co_no = dic['fin_co_no']
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

            # 옵션의 외래키는 api response에서 가져올 수 없으므로 직접 입력한다.
            product = Fixed.objects.get(fixed_code=fin_prdt_cd, fin_co_no=fin_co_no)  # 외래키가 참조하는 상품 조회
            serializer = FixedOptionsSerializer(data=save_data)
            
            if serializer.is_valid(raise_exception=True):
                serializer.save(product=product)    # 저장하는 과정에서 외래키를 입력

    return JsonResponse({'message' : 'save Fixed complete!'})


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def save_installment(request):
    ## (1) 1금융권 상품 목록 저장
    url = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'

    # API 데이터 조회
    response = requests.get(url).json()
    
    # Installment 적금 상품 목록을 순회하며 저장
    for dic in response.get('result').get('baseList'):
        fin_co_no = dic['fin_co_no']
        kor_co_nm = dic['kor_co_nm']
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
            'fin_grp_no': 1,
            'fin_co_no': fin_co_no,
            'kor_co_nm': kor_co_nm,
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
        
        # 중복 저장 방지
        if Installment.objects.filter(kor_co_nm=kor_co_nm, installment_code=installment_code).exists():
            return JsonResponse({'message' : 'Data already stored'})
            
        # 직렬화 및 유효성검사 후 저장
        serializer = InstallmentSerializer(data=save_data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

    # InstallmentOption 적금 상품 옵션 목록을 순회하며 저장
    for dic in response.get('result').get('optionList'):
        fin_prdt_cd = dic['fin_prdt_cd']
        fin_co_no = dic['fin_co_no']
        intr_rate_type_nm = dic['intr_rate_type_nm']
        save_trm = dic['save_trm']
        intr_rate = dic['intr_rate']
        intr_rate2 = dic['intr_rate2']
        rsrv_type_nm = dic['rsrv_type_nm']

        save_data = {
            'intr_rate_type_nm': intr_rate_type_nm,
            'rsrv_type_nm': rsrv_type_nm,
            'save_trm': save_trm,
            'intr_rate': intr_rate,
            'intr_rate2': intr_rate2,
        }

        # 옵션의 외래키는 api response 데이터에서 가져올 수 없으므로 직접 입력
        product = Installment.objects.get(installment_code=fin_prdt_cd, fin_co_no=fin_co_no)  #외래키가 참조하는 상품 조회
        serializer = InstallmentOptionsSerializer(data=save_data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save(product=product)    # 저장하는 과정에서 외래키를 입력


     ## (2) 저축은행 상품 목록 저장
    for num in range(1, 5):
        url = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={api_key}&topFinGrpNo=030300&pageNo={num}'

        # API 데이터 조회하여 request 객체 생성
        response = requests.get(url).json()
        
        # Fixed 정기예금 상품 목록을 순회하며 저장
        for dic in response.get('result').get('baseList'):
            fin_co_no = dic['fin_co_no']
            kor_co_nm = dic['kor_co_nm']
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
                'fin_grp_no': 2,
                'fin_co_no': fin_co_no,
                'kor_co_nm': kor_co_nm,
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
            
            # 중복 저장 방지
            if Installment.objects.filter(fin_co_no=fin_co_no, installment_code=installment_code).exists():
                return JsonResponse({'message' : 'Data already stored'})
                
            # 직렬화 및 유효성검사 후 저장
            serializer = InstallmentSerializer(data=save_data)

            if serializer.is_valid(raise_exception=True):
                serializer.save()

        # InstallmentOption 정기예금 상품 옵션 목록을 순회하며 저장
        for dic in response.get('result').get('optionList'):
            fin_prdt_cd = dic['fin_prdt_cd']
            fin_co_no = dic['fin_co_no']
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

            # 옵션의 외래키는 api response에서 가져올 수 없으므로 직접 입력한다.
            product = Installment.objects.get(installment_code=fin_prdt_cd, fin_co_no=fin_co_no)  # 외래키가 참조하는 상품 조회
            serializer = InstallmentOptionsSerializer(data=save_data)
            
            if serializer.is_valid(raise_exception=True):
                serializer.save(product=product)    # 저장하는 과정에서 외래키를 입력

    return JsonResponse({'message' : 'save Installment complete!'})


# ----------- 조회 -----------

# [GET] 전체 정기예금 상품 조회
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_fixed(request):
    if request.method == 'GET':
        fixed = Fixed.objects.all()
        serializer = FixedSerializer(fixed, many=True)
        return Response(serializer.data)
    
# [GET] 전체 정기예금 상품 옵션 조회
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_fixedOption(request):
    if request.method == 'GET':
        fixedoption = FixedOption.objects.all()
        serializer = FixedOptionsSerializer(fixedoption, many=True)
        return Response(serializer.data)
    
# [GET] 전체 적금 상품 조회
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_installment(request):
    if request.method == 'GET':
        installment = Installment.objects.all()
        serializer = InstallmentSerializer(installment, many=True)
        return Response(serializer.data)    

# [GET] 전체 적금 상품 옵션 조회
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_installmentOption(request):
    if request.method == 'GET':
        installmentoption = InstallmentOption.objects.all()
        serializer = InstallmentOptionsSerializer(installmentoption, many=True)
        return Response(serializer.data)
    
    
# [GET] 단일 정기예금 상품 상세조회
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def detail_fixed(request, product_id):
    fixed = get_object_or_404(Fixed, id=product_id)
    serializer = FixedSerializer(fixed)
    return Response(serializer.data, status=status.HTTP_200_OK)


# [GET] 단일 정기적금 상품 상세조회
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def detail_installment(request, product_id):
    installment = get_object_or_404(Installment, id=product_id)
    serializer = InstallmentSerializer(installment)
    return Response(serializer.data, status=status.HTTP_200_OK)


# ----------- 상품 가입 및 탈퇴 -----------

# [POST] 정기예금 상품 가입 및 탈퇴
@api_view(['POST','DELETE'])
@permission_classes([IsAuthenticated])
def join_fixed(request, username, product_id):
    usermodel = get_user_model().objects.get(username=username)
    fixed = Fixed.objects.get(id=product_id)
    
    if request.method == 'POST':
        usermodel.fixed.add(fixed)
        serializer = UserInfoSerializer(usermodel)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'DELETE':
        usermodel.fixed.remove(fixed)
        serializer = UserInfoSerializer(usermodel)
        return Response(serializer.data, status=status.HTTP_200_OK)


# [POST] 적금 상품 가입 및 탈퇴
@api_view(['POST','DELETE'])
@permission_classes([IsAuthenticated])
def join_installment(request, username, product_id):
    usermodel = get_user_model().objects.get(username=username)
    installment = Installment.objects.get(id=product_id)
    
    if request.method == 'POST':
        usermodel.installment.add(installment)
        serializer = UserInfoSerializer(usermodel)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        usermodel.installment.remove(installment)
        serializer = UserInfoSerializer(usermodel)
        return Response(serializer.data, status=status.HTTP_200_OK)
