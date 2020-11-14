from rest_framework import serializers

from ccas.models import Cca


class CcaSerializer(serializers.ModelSerializer):
    students = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Cca
        fields = ('id', 'name', 'description', 'students')
