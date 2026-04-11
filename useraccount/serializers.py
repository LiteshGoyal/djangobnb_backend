from rest_framework import serializers

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