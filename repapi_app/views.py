# api/views.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_data(request):
    # Gracias a @permission_classes([IsAuthenticated]),
    # esta vista solo se ejecuta si se envía un token válido.
    # El usuario autenticado está en 'request.user'.
    user = request.user
    return Response({
        'message': f'¡Hola, {user.username}! Estos son tus datos protegidos.',
        'email': user.email
    })