from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer
from .models import Article, Comment


 # articles의 함수들은 로그인(인증) 사용자만 접근

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def index(request):
    # [GET] 전체 게시글목록 조회
    if request.method == 'GET':
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    # [POST] 게시글 작성
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user = request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    # [GET] 단일 게시글 상세 조회
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    # [DELETE] 게시글 삭제
    elif request.method == 'DELETE':
        # 작성자 확인
        if request.user == article.user:
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    
    # [PUT] 게시글 수정
    elif request.method == 'PUT':
        # 작성자 확인
        if request.user == article.user:
            serializer = ArticleSerializer(article, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        

# [POST] 게시글에 댓글 등록
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comments_create(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article, user = request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def comments_detail(request, article_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    # [GET] 단일 댓글 조회
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # [DELETE] 댓글 삭제
    elif request.method == 'DELETE':
        # 사용자 인증
        if request.user == comment.user:
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    
    # [PUT] 댓글 수정
    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        # 사용자 인증
        if request.user == comment.user:
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)



