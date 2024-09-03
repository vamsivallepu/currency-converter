from rest_framework.decorators import api_view
from .serializers import RegistrationSerializer
from rest_framework.response import Response

# Create your views here.
@api_view(['POST'])
def registrantion_view(request):
     if request.method == "POST":
          serializer = RegistrationSerializer(data=request.data)
          if serializer.is_valid():
               serializer.save()
               return Response({"message": "Registered Successfully. "})
          else:
               return Response({"message": "Something Went wrong. "})
