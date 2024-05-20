from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    # [GET] 전체 정기예금 상품 및 상품 옵션 저장
    path('save-fixed/', views.save_fixed),

    # [GET] 전체 적금 상품 및 상품 옵션 저장
    path('save-installment/', views.save_installment),
    
    # [GET] 전체 정기예금 상품 조회
    path('get-fixed/', views.get_fixed),
    
    # [GET] 전체 정기예금 상품 옵션 조회
    path('get-fixedOption/', views.get_fixedOption),
    
    # [GET] 전체 적금 상품 조회
    path('get-installment/', views.get_installment),
    
    # [GET] 전체 적금 상품 옵션 조회
    path('get-installmentOption/', views.get_installmentOption),
]
