from rest_framework import serializers

from drapi.models import Aiquest


# python

class AiquestSerializer(serializers.ModelSerializer):
    teacher_name = serializers.CharField(max_length=25)
    course_name = serializers.CharField(max_length=20)
    course_duration = serializers.IntegerField()
    seat = serializers.IntegerField()

    class Meta:
        model = Aiquest
        fields = '__all__'

#Deserializers
def create(self, validated_data):
    return Aiquest.objects.create(**validated_data)
