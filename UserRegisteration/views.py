from rest_framework import generics, response, status
from rest_framework.authtoken.models import Token
from .serializer import UserRegistrationSerializer

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests for user registration.

        Parameters:
        - request (Request): The incoming request object containing user data.
        - args (tuple): Additional positional arguments.
        - kwargs (dict): Additional keyword arguments.

        Returns:
        - Response: A response object containing the generated token upon successful registration.
                    If registration fails, returns a response object with the error details.

        Raises:
        - None

        """
        # Serialize the incoming request data
        serializer = self.get_serializer(data=request.data)

        # Check if the serialized data is valid
        if serializer.is_valid():
            # Save the user data and create a new user object
            user = serializer.save()

            # Generate or retrieve an authentication token for the newly created user
            token, _ = Token.objects.get_or_create(user=user)

            # Return a response with the generated token and a success status code
            return response.Response({'token': token.key}, status=status.HTTP_201_CREATED)

        # If the serialized data is not valid, return a response with the error details and a bad request status code
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
