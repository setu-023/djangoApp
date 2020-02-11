from rest_framework import serializers

from user_profile.models import User_Profile


class RegistrationSerializer(serializers.ModelSerializer):

	password_confirmation				= serializers.CharField(style={'input_type': 'password'}, write_only=True)

	class Meta:
		model = User_Profile
		fields = ['email', 'username', 'password', 'password_confirmation']
		extra_kwargs = {
				'password': {'write_only': True},
		}


	def	save(self):

		user_profile = User_Profile(
					email=self.validated_data['email'],
					username=self.validated_data['username'],
                #    role    =self.validated_data['role']
				)
		password = self.validated_data['password']
		password_confirmation = self.validated_data['password_confirmation']
		if password != password_confirmation:
			raise serializers.ValidationError({'password': 'Passwords must match.'})
		user_profile.set_password(password)
		user_profile.save()
		return user_profile
