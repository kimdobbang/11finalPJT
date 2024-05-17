from allauth.account.adapter import DefaultAccountAdapter

class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        
        data = form.cleaned_data
        user = super().save_user(request, user, form, False)
        
        # first_name = data.get("first_name")
        # last_name = data.get("last_name")
        # email = data.get("email")
        # username = data.get("username")
        # 필드를 추가
        nickname = data.get("nickname")
        profile_img = data.get("profile_img")
        age = data.get("age")
        money = data.get("money")
        salary = data.get("salary")
        
        if nickname:
            user.nickname = nickname
        if profile_img:
            user.profile_img = profile_img
        if age:
            user.age = age
        if money:
            user.money = money
        if salary:
            user.salary = salary
            
        # if "password1" in data:
        #     user.set_password(data["password1"])
        # else:
        #     user.set_unusable_password()
        # self.populate_username(request, user)
        
        if commit:
            user.save()
            
        return user