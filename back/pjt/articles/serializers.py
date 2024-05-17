from rest_framework import serializers
from .models import Article, Comment

# 전체 목록
class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content',) # 3개 필드만 제공


# 단일 게시글
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user',)
        

# 댓글은 serializer 하나로
# 댓글 목록 조회를 위한 CommentSerializer 정의
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('user', 'article',)  # is valid검사 목록에선 제외하고 제공