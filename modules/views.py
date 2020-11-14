import django.db as db
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from modules.models import Module
from modules.serializers import ModuleSerializer
from students.models import Student


class ModuleList(generics.ListCreateAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer


class ModuleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer


@api_view(['POST'])
def add_students(request, pk):
    try:
        students = request.data['students']
        if isinstance(students, str):
            raise TypeError
        for student in students:
            if not isinstance(student, str):
                raise TypeError
    except (KeyError, TypeError):
        return Response({"message": "Invalid request format"}, 502)

    try:
        m = Module.objects.get(pk=pk)

        for student in students:
            try:
                Student.objects.get(pk=student)
            except Student.DoesNotExist:
                return Response({"message": "Student {} does not exist".format(student)},
                                status=404)

            m.students.add(student)

        m.save()

        new_list = []
        for student in m.students.all():
            new_list.append(student.matriculation_number)

        return Response({'message': 'Success',
                        'students': new_list}, status=200)
    except Module.DoesNotExist:
        return Response({"message": "Module {} does not exist".format(pk)},
                        status=404)
    except db.utils.IntegrityError:
        return Response({"message": "Unable to save"}, status=500)





