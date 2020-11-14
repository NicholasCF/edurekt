from django.db import models

from modules.models import Module
from ccas.models import Cca


class Student(models.Model):
    matriculation_number = models.CharField(primary_key=True, max_length=9, blank=False)
    name = models.CharField(max_length=256, blank=False)
    year = models.PositiveSmallIntegerField(blank=False, default=1)
    course = models.CharField(max_length=256, blank=False)

    modules = models.ManyToManyField(Module, related_name='students', through='TakeModule')
    ccas = models.ManyToManyField(Cca, related_name='students', through='Membership')

    def __str__(self):
        return "{} ({})".format(self.name, self.matriculation_number)


class TakeModule(models.Model):
    module = models.ForeignKey(Module, related_name='module_to_student', on_delete=models.CASCADE)
    student = models.ForeignKey(Student, related_name='student_to_module', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('module', 'student')


class Membership(models.Model):
    cca = models.ForeignKey(Cca, related_name='cca_to_student', on_delete=models.CASCADE)
    student = models.ForeignKey(Student, related_name='student_to_cca', on_delete=models.CASCADE)

    membership_status = models.CharField(max_length=1, choices=(('M', 'Member'), ('L', 'Leader')), blank=False)

    class Meta:
        unique_together = ('cca', 'student')
