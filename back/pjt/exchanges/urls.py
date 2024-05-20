from django.urls import path
from . import views

app_name = 'exchanges'
urlpatterns = [
    # [GET] 전체 환율 정보 저장
    path('save-exchange/', views.save_exchange),
    
    # [GET] 전체 환율 정보 조회
    path('get-exchange/', views.get_exchange),
]
