from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import User

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =(
            'id','email', 'name', 'avatar_url'
        )
    def get_avatar_url(self, obj):
        if obj.avatar:
            return f"{settings.WEBSITE_URL}{obj.avatar.url}"
        return ""
    

class CustomRegisterSerializer(RegisterSerializer):
    name = serializers.CharField(required=True)

    def custom_signup(self, request, user):
        print("🔥 CUSTOM SIGNUP RUNNING")
        # 🔥 THIS is the correct place to set extra fields
        user.name = self.validated_data.get('name')
        user.save(update_fields=['name'])