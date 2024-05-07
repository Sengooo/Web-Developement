from rest_framework import generics, status
from django.contrib.auth import get_user_model, authenticate
from .serializers import UserSerializer, ProductSerializer, CreditCardSerializer, CartSerializer
from .models import Product, CreditCard, Cart, User
from rest_framework_jwt.views import ObtainJSONWebToken
from rest_framework.response import Response
from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler
from rest_framework_jwt.settings import api_settings

User = get_user_model()

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CreditCardListView(generics.ListAPIView):
    queryset = CreditCard.objects.all()
    serializer_class = CreditCardSerializer

class CreditCardDetailView(generics.RetrieveAPIView):
    queryset = CreditCard.objects.all()
    serializer_class = CreditCardSerializer

class CartList(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CustomObtainJSONWebToken(ObtainJSONWebToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainJSONWebToken, self).post(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            token = response.data['token']
            jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
            user_id = jwt_decode_handler(token)['user_id']
            user = User.objects.get(id=user_id)
            user_serializer = UserSerializer(user, context={'request': request})
            response.data['user'] = user_serializer.data
        return response

class RegisterPageAPIView(ObtainJSONWebToken):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.create(serializer.validated_data).get('username')

        auth_user = authenticate(username=username, password=request.data['password'])
        if auth_user is None:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        payload = jwt_payload_handler(auth_user)
        token = jwt_encode_handler(payload)

        response = Response({'token': token, 'user': serializer.data}, status=status.HTTP_201_CREATED)

        return response