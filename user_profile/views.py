# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
#
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated
# from django.views.decorators.csrf import csrf_exempt
# from django.contrib.auth import authenticate
# from user_profile.serializers import RegistrationSerializer
# from rest_framework.authtoken.models import Token
#
# from rest_framework.status import (
#     HTTP_400_BAD_REQUEST,
#     HTTP_404_NOT_FOUND,
#     HTTP_200_OK
# )
#
#
# @api_view(['POST', ])
# def registration_view(request):
#
# 	if request.method == 'POST':
# 		serializer = RegistrationSerializer(data=request.data)
# 		data = {}
# 		if serializer.is_valid():
# 			account = serializer.save()
# 			data['response'] = 'successfully registered new user.'
# 			data['email'] = account.email
# 			data['username'] = account.username
# 			#data['role'] = account.role
# 			#token = Token.objects.get(user=account).key
# 			#data['token'] = token
# 		else:
# 			data = serializer.errors
# 		return Response(data)
