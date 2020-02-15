from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import BasePermission, IsAuthenticated, IsAdminUser
from django.contrib.auth.decorators import permission_required
from account.models import Account
from rest_framework.decorators import api_view, permission_classes

# from account.permission import HRAdminGroupPermission
from account.api.serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token

# Register
# Response: https://gist.github.com/mitchtabian/c13c41fa0f51b304d7638b7bac7cb694
# Url: https://<your-domain>/api/account/register

@api_view(['POST', ])
def registration_view(request):

	if request.method == 'POST':
		serializer = RegistrationSerializer(data=request.data)
		data = {}
		if serializer.is_valid():
			account = serializer.save()
			data['response'] = 'successfully registered new user.'
			data['email'] = account.email
			data['username'] = account.username
			token = Token.objects.get(user=account).key
			data['token'] = token
		else:
			data = serializer.errors
		return Response(data)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def sample(self):

	data={'msg':'hello'}

	group_required = 'HR Admin1'
	return Response(data)
