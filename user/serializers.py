from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers

# from django.contrib.auth.models import User
# from user.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

MAX_LEN_PASSWORD = 128

class UserSerializer(serializers.ModelSerializer):
  # associates = AssociateSerializer(read_only=True, many=True)
  
  class Meta:
    model = User
    fields = [ 'id', 'username', 'first_name', 'last_name', 'job_title']

class OwnerSerializer(serializers.ModelSerializer):

  class Meta:
    model = User
    fields = ['id', 'email', 'username', 'first_name', 'last_name', 'job_title']

class UserUpdateSerializer(serializers.ModelSerializer):
  id = serializers.IntegerField(read_only=True)
  # username = serializers.CharField(read_only=True)
  email = serializers.EmailField(read_only=True)

  class Meta:
    model = User
    fields = ['id', 'email', 'username', 'first_name', 'last_name', 'job_title']

    
class ChangePasswordSerializer(serializers.Serializer):
  old_password = serializers.CharField(max_length=MAX_LEN_PASSWORD, write_only=True, required=True)
  new_password1 = serializers.CharField(max_length=MAX_LEN_PASSWORD, write_only=True, required=True)
  new_password2 = serializers.CharField(max_length=MAX_LEN_PASSWORD, write_only=True, required=True)

  def validate_old_password(self, value):
    user = self.instance
    if not user.check_password(value):
      raise serializers.ValidationError(
        _('Incorrect old password.')
      )
    return value

  def validate(self, data):
    if data['new_password1'] != data['new_password2']:
      raise serializers.ValidationError(_("Passwords doesn't match"))
    # password_validation.validate_password(data['new_password1'], self.context['request'].user)
    return data

  def save(self, **kwargs):
    password = self.validated_data['new_password1']
    user = self.instance
    user.set_password(password)
    user.save()
    return user 
