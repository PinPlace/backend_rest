from .serializers import UserSerializer
# from .serializers import RegistrationSerializer
from rest_framework import viewsets, permissions
from django.contrib.auth.models import User
# from .forms import UserSignupForm
# from rest_framework.response import Response
# from rest_framework.decorators import api_view

# Create your views here.

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
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