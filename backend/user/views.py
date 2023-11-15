from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import AccessToken
from datetime import datetime
from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from django.contrib.auth.hashers import make_password


from .models import User
from .serializers import CustomTokenObtainPairSerializer, UserFullSerializer
from .filters import UserFilter


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        # if response.status_code == status.HTTP_200_OK:
        #     response = Response(
        #         {"detail": "Account not activated."},
        #         status=status.HTTP_401_UNAUTHORIZED,  # Change to 401
        #     )
        return response


class VerifyToken(APIView):
    def get(self, request, format=None):
        token = request.data.get("token", "")

        if token:
            try:
                access_token = AccessToken(token)
                expiration_timestamp = access_token.payload["exp"]
                expiration_datetime = datetime.fromtimestamp(expiration_timestamp)

                is_expired = expiration_datetime < datetime.now()

                return Response({"is_expired": is_expired})
            except Exception as e:
                return Response({"error": str(e)})
        else:
            return Response({"error": "Token not provided"})


class ResetPassword(APIView):
    def post(self, request, format=None):
        id = request.data.get("id")
        new_password = request.data.get("new_password")

        account = User.objects.filter(id=id).first()
        account.set_password(new_password)
        account.save()

        response_data = {
            "message": "Account password reset successful",
        }
        return Response(response_data, status=status.HTTP_200_OK)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserFullSerializer
    filterset_class = UserFilter

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        account_data = {
            "username": request.data.get("username"),
            "name": request.data.get("name"),
            "password": make_password(request.data.get("password")),
            "email": request.data.get("email"),
            "role": "Staff",
        }
        account_serializer = UserFullSerializer(data=account_data)
        account_serializer.is_valid(raise_exception=True)
        account_serializer.save()

        response_data = {
            "message": "Account created successfully",
        }
        return Response(response_data, status=status.HTTP_201_CREATED)


class UserSpecificView(generics.RetrieveAPIView):
    lookup_field = "id"
    queryset = User.objects.all()
    serializer_class = UserFullSerializer

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class ToggleUserActivation(APIView):
    def post(self, request, *args, **kwargs):
        user_id = request.data.get("user_id")  # Get the user_id from the request data

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response(
                {"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND
            )

        # Toggle the is_active status
        user.is_active = not user.is_active

        user.save()

        return Response(
            {"detail": "User activation status toggled successfully."},
            status=status.HTTP_200_OK,
        )