from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer
from django.contrib.auth import get_user_model



UserModel = get_user_model()

class CustomRegisterSerializer(RegisterSerializer):
    # 기본 설정 필드: username, password, email
    # 추가 설정 필드: nickname, profile_img, age, money, salary
    nickname = serializers.CharField(max_length=100)
    profile_img = serializers.ImageField(use_url=True, required=False)  # 파일 필드이므로 required=False로 설정
    age = serializers.IntegerField()
    money = serializers.IntegerField()
    salary = serializers.IntegerField()
    
    class Meta:
        model = UserModel
        fields = ('username', 'password1', 'password2', 'email', 'nickname', 'profile_img', 'age', 'money', 'salary')

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['nickname'] = self.validated_data.get('nickname', '')
        data['profile_img'] = self.validated_data.get('profile_img', None)  # None을 기본값으로 설정하여 없을 경우를 처리
        data['age'] = self.validated_data.get('age', '')
        data['money'] = self.validated_data.get('money', '')
        data['salary'] = self.validated_data.get('salary', '')
        
        return data
    

class CustomUserDetailsSerializer(UserDetailsSerializer):
    class Meta:
        extra_fields = []
        if hasattr(UserModel, 'USERNAME_FIELD'):
            extra_fields.append(UserModel.USERNAME_FIELD)
        if hasattr(UserModel, 'EMAIL_FIELD'):
            extra_fields.append(UserModel.EMAIL_FIELD)
        if hasattr(UserModel, 'first_name'):
            extra_fields.append('first_name')
        if hasattr(UserModel, 'last_name'):
            extra_fields.append('last_name')
        if hasattr(UserModel, 'nickname'):
            extra_fields.append('nickname')
        if hasattr(UserModel, 'profile_img'):
            extra_fields.append('profile_img')
        if hasattr(UserModel, 'age'):
            extra_fields.append('age')
        if hasattr(UserModel, 'money'):
            extra_fields.append('money')
        if hasattr(UserModel, 'salary'):
            extra_fields.append('salary')
            
        model = UserModel
        fields = ('pk', *extra_fields)
        read_only_fields = ('email',)
