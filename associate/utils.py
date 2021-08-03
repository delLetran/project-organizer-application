from .serializers import UserSerializer

def get_mutual_associates_list(user, *args, **kwargs):
  mutual_associates_list = []
  mutuals_list = user.get_associate_with_mutual_associates_list() 
  
  for (profile, mutuals) in mutuals_list:
    serialized_profile = UserSerializer(profile)
    serializer_mutuals = UserSerializer(mutuals, many=True)
    data = {
      'profile': serialized_profile.data,
      'mutual_associates': serializer_mutuals.data
    }
    mutual_associates_list.append(data)
  return mutual_associates_list