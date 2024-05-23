from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    
    # ----------- 저장 -----------
    
    # [GET] 전체 정기예금 상품 및 상품 옵션 저장
    path('save-fixed/', views.save_fixed),

    # [GET] 전체 적금 상품 및 상품 옵션 저장
    path('save-installment/', views.save_installment),
    
    
    # ----------- 조회 -----------
    
    # [GET] 전체 정기예금 상품 조회
    path('get-fixed/', views.get_fixed),
    
    # [GET] 전체 정기예금 상품 옵션 조회
    path('get-fixedOption/', views.get_fixedOption),
    
    # [GET] 전체 적금 상품 조회
    path('get-installment/', views.get_installment),
    
    # [GET] 전체 적금 상품 옵션 조회
    path('get-installmentOption/', views.get_installmentOption),
    
    # [GET] 단일 정기예금 상품 상세조회
    path('fixed/<int:product_id>/', views.detail_fixed),

    # [GET] 단일 정기적금 상품 상세조회
    path('installment/<int:product_id>/', views.detail_installment),
    

    # ----------- 상품 가입 및 탈퇴 -----------
    
    # [POST] 정기예금 상품 가입
    # [DELETE] 정기예금 상품 탈퇴
    path('fixed/<str:username>/<int:product_id>/', views.join_fixed),

    # [POST] 정기적금 상품 가입
    # [DELETE] 정기적금 상품 탈퇴
    path('installment/<str:username>/<int:product_id>/', views.join_installment),
    
    # ----------- 상품 추천 -----------
    
    # [GET] 정기예금, 적금 상품 추천
    path('recommend/<str:username>/', views.recommend),

]
