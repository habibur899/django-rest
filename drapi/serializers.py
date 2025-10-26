from rest_framework import serializers

from drapi.models import Aiquest


class AiquestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aiquest
        fields = '__all__'

