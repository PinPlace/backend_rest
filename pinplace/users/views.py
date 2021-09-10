from .serializers import UserSerializer
from rest_framework import mixins, viewsets, permissions
from django.contrib.auth import get_user_model

User = get_user_model()

# ViewSets define the view behavior.
class AuthViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

# def registration_view(request):
#     if request.method == "POST ":
#         serializer = RegistrationSerializer(data=request.data)
#         data = {}
#         if serializer.is_valid():
#             user = serializer.save()
#             data['response'] = "successfully registered a new user"
#             data['email'] = user.email
#             data['username'] = user.username
#         else:
#             data = serializers.errors
#         return Response(data)

# def signup(request):
#     if request.method == 'POST':
#         new_user = UserSignupForm(request.POST)
#         if new_user.is_valid():
#             new_user.save()
#             return redirect('inventory-index')
#     else:
#         form = UserSignupForm()
#         context = { "form": form }
#         return render(request, 'users/signup.html', context)