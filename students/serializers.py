from rest_framework import serializers

from ccas.models import Cca
from modules.models import Module
from students.models import Student, TakeModule, Membership


class StudentSerializer(serializers.ModelSerializer):
    modules = serializers.PrimaryKeyRelatedField(many=True, queryset=Module.objects.all(), read_only=False)
    ccas = serializers.SlugRelatedField(many=True, queryset=Cca.objects.all(), read_only=False, slug_field='name')

    class Meta:
        model = Student
        fields = ('matriculation_number', 'name', 'year', 'course', 'modules', 'ccas')


class TakeModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TakeModule
        fields = ('module', 'student')
