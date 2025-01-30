from .models import Teachers,students
import rest_framework.serializers as serializers

class TeachersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Teachers
        fields='__all__'

class studentsSerializer(serializers.ModelSerializer):
    class Meta:
        model=students
        fields='__all__'
