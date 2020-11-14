from django.contrib import admin

from students.models import Membership, Student, TakeModule


# NOT to be confused with admin.register
admin.site.register(Membership)
admin.site.register(Student)
admin.site.register(TakeModule)
