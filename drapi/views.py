from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from .models import Aiquest
from .serializers import AiquestSerializer


def aiquest_info(request):
    # Complex data
    ai = Aiquest.objects.all()
    # Python dictionary
    serializer = AiquestSerializer(ai, many=True)
    # Render JSON
    json_data = JSONRenderer().render(serializer.data)
    # JSON sent to User
    return HttpResponse(json_data, content_type='application/json')


def aiquest_info_single(request, pk):
    # Complex data
    ai = Aiquest.objects.get(id=pk)
    # Python dictionary
    serializer = AiquestSerializer(ai)
    # Render JSON
    json_data = JSONRenderer().render(serializer.data)
    # JSON sent to User
    return HttpResponse(json_data, content_type='application/json')
