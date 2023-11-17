from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers

class CustomRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(required=True)
    age = serializers.IntegerField(required=True)
    mbti = serializers.CharField(required=False)

    def save(self, request):
        user = super().save(request)
        user.nickname = self.validated_data.get('nickname', '')
        user.age = self.validated_data.get('age', 0)
        user.mbti = self.validated_data.get('mbti', '')
        user.save()
        return user