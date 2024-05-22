from django.shortcuts import render
from django.contrib.auth import get_user_model
from .serializers import UserInfoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.
@api_view(['GET']) 
def getuser(request ,username):
    usermodel = get_user_model().objects.get(username=username)
    serializer = UserInfoSerializer(usermodel)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET']) 
def allusers(request ,username):
    usermodel = get_user_model().objects.all()
    serializer = UserInfoSerializer(usermodel, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET']) 
def makeusers(request):
    # 랜덤한 더미 데이터를 만드는 파일입니다.
    # 반드시 금융 상품 데이터를 DB에 저장한 후에 진행할 것
    from products.models import Fixed
    from products.models import Installment
    from django.contrib.auth import get_user_model

    import random
    import requests

    first_name_samples = '김이박최정강조윤장임'
    middle_name_samples = '민서예지도하주윤채현지'
    last_name_samples = '준윤우원호후서연아은진'


    def random_name():
        result = ''
        result += random.choice(first_name_samples)
        result += random.choice(middle_name_samples)
        result += random.choice(last_name_samples)
        return result + str(random.randint(1, 100))

    fixed_list = list(Fixed.objects.all())
    installment_list = list(Installment.objects.all())


    dict_keys = [
        'username',
        'gender',
        'fixed',
        'installment',
        'age',
        'money',
        'salary',
    ]

    # json 파일 만들기
    import json
    from collections import OrderedDict

    file = OrderedDict()

    username_list = []
    N = 200
    i = 0

    while i < N:
        rn = random_name()
        if rn in username_list:
            continue

        username_list.append(rn)
        i += 1


    # 저장 위치는 프로젝트 구조에 맞게 수정합니다.
    save_dir = './user_data.json'
    with open(save_dir, 'w', encoding="utf-8") as f:
        f.write('[')

        for i in range(N):
            # 랜덤한 데이터를 삽입
            file['model'] = 'accounts.User'
            file['pk'] = i + 1
            file['fields'] = {
                'username': username_list[i],  # 유저 이름 랜덤 생성
                # 랜덤한 0~2개의 상품을 가입하도록 삽입됨
                'fixed': [
                        random.choice(fixed_list).id
                        for _ in range(random.randint(0, 2))
                    ], # 금융 상품 정기예금 리스트
                'installment': [
                        random.choice(installment_list).id
                        for _ in range(random.randint(0, 5))
                    ], # 금융 상품 적금 리스트
                'age': random.randint(1, 100),  # 나이
                'money': random.randrange(0, 100000000, 100000),  # 현재 가진 금액
                'salary': random.randrange(0, 1500000000, 1000000),  # 연봉
                'password': '1234',
                'nickname': None,
                'is_active': True,
                'is_staff': False,
                'is_superuser': False,
            }

            json.dump(file, f, ensure_ascii=False, indent='\t')
            if i != N - 1:
                f.write(',')
        f.write(']')
        f.close()

    print(f'데이터 생성 완료 / 저장 위치: {save_dir}')
    return
