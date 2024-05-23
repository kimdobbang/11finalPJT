from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    #-------게시글------------
    # [GET] 전체 게시글목록 조회
    # [POST] 게시글 작성 
    path('', views.index),

    # [GET] 단일 게시글 상세 조회
    # [PUT] 게시글 수정
    # [DELETE] 게시글 삭제
    path('<int:article_id>/', views.detail),

    #-------댓글--------------
    # [GET] 전체 댓글 조회
    # [POST] 게시글에 댓글 등록
    path('<int:article_id>/comment/', views.comments_create),

    # [GET] 단일 댓글 조회
    # [DELETE] 댓글 삭제
    # [PUT] 댓글 수정
    path('<int:article_id>/comment/<int:comment_id>/', views.comments_detail),
]
