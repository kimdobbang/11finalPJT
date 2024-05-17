from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
class CustomUserAdmin(UserAdmin):
    # UserAdmin의 fieldsets에 새로운 필드를 추가합니다.
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('nickname', 'profile_img', 'age', 'money', 'salary', 'fixed', 'installment')}),
    )
    # 어드민 사이트의 사용자 추가 페이지에서 보여질 필드를 추가합니다.
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('nickname', 'profile_img', 'age', 'money', 'salary')}),
    )

admin.site.register(User, CustomUserAdmin)