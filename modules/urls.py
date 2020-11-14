from django.urls import path

from modules.views import add_students, ModuleDetail, ModuleList

urlpatterns = [
    path('modules', ModuleList.as_view()),
    path('modules/<str:pk>', ModuleDetail.as_view()),
    path('modules/<str:pk>/add_students', add_students)
]
