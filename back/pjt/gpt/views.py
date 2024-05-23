from django.conf import settings
from django.http import JsonResponse 
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
import openai
import json

openai.api_key = settings.OPENAI_API_KEY

def get_completion(prompt): 
    print(prompt) 
    query = openai.ChatCompletion.create( 
        model="gpt-4",
        messages=[
            {'role': 'system', 'content': '저는 고객 맞춤형 금융상품 추천 전문가 파이냠냠!. 당신의 재무 상황과 목표에 따라 최적의 금융상품을 추천해드립니다냠♥'},
            {'role': 'assistant', 'content': '안녕하세냠! 당신의 재무 상황과 목표에 따라 최적의 금융상품을 추천해드리겠습니냠. 먼저 몇 가지 질문을 통해 정보를 얻고자 한다냠♥'},
            {"role": "user", "content": "자신의 상황에 맞는 금융상품 추천을 요청합니다."},
            {'role': 'assistant', 'content': '당신의 나이와 현재 소득 수준을 알려주시겠어요? 또한 어떤 금융상품(예: 저축, 투자, 보험 등)에 관심이 있으신가냠♥?'},
            {"role": "user", "content": "추천 금융상품 세부 정보에 관해 재차 물어봅니다."},
            {'role': 'assistant', 'content': '국민은행에서 제공하는 정기적금 중에서는 KB Star 정기적금이 인기가 있습니냠. 이 상품은 다음과 같은특징을 가지고 있습니냠.\n 1. 가입 최저 금액: 월 2만 원\n2. 가입 기간: 6개월 ~ 36개월\n3. 금리: 기간에 따라 다르지만, 최대 연 1.80% 이다냠.\n금리는 시장 상황에 따라 변동될 수 있으니, 직접 은행에 문의하시는 것이 가장 정확합니냠♥'},
            {'role': 'user', 'content': prompt},
        ], 
        max_tokens=1000,
        n=1, 
        stop=None, 
        temperature=0.5, 
    ) 
    response = query.choices[0].message["content"]
    print(response) 
    return response 

@api_view(['POST'])
def query_view(request): 
    if request.method == 'POST': 
        print(request.data)
        prompt = request.data.get('prompt')
        response = get_completion(prompt)
        return JsonResponse({'response': response})
    return Response({'error': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
