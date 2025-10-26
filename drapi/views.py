import io

from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from .models import Aiquest
from .serializers import AiquestSerializer
from django.views.decorators.csrf import csrf_exempt


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


# Deserializers
@csrf_exempt
def aiquest_create(request):
    if request.method == 'POST':
        json_data = request.body
        # JSON to Stream
        stream = io.BytesIO(json_data)
        # Stream to Python
        pythondata = JSONParser().parse(stream)
        # Python to complex
        serializer = AiquestSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Successfully! insert data'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    # Update data
    if request.method == 'PUT':
        json_data = request.body
        # JSON to Stream
        stream = io.BytesIO(json_data)
        # Stream to Python
        pythondata = JSONParser().parse(stream)
        # Get object
        ai = Aiquest.objects.get(id=pythondata['id'])
        # Python to complex
        serializer = AiquestSerializer(ai, data=pythondata, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Successfully! Updated data'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
