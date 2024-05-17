from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer
from .models import Article, Comment


# [GET] 전체 게시글목록 조회
@api_view(['GET', 'POST']) 
def index(request):
    # [GET] 전체 게시글목록 조회
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    # [POST] 게시글 작성
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user = request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def detail(request, article_id):
    article = Article.objects.get(pk=article_id)

    # [GET] 단일 게시글 상세 조회
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    # [DELETE] 게시글 삭제
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    # [PUT] 게시글 수정
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        

# [POST] 게시글에 댓글 등록
@api_view(['POST'])
def comments_create(request, article_id):
    article = Article.objects.get(pk=article_id)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article, user = request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# [PUT] 댓글 수정
@api_view(['GET', 'DELETE', 'PUT'])
def comments_detail(request, article_id, comment_id):
    comment = Comment.objects.get(pk=comment_id)

    # [GET] 단일 댓글 조회
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    # [DELETE] 댓글 삭제
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    # [PUT] 댓글 수정
    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)



