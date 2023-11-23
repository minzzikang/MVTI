from dj_rest_auth.registration.views import RegisterView
from .serializers import UserUpdateSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
# class CustomRegisterView(RegisterView):
#     serializer_class = CustomRegisterSerializer

@api_view(['POST'])
def userupdate (request):
    serializer = UserUpdateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)