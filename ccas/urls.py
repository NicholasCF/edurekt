from django.urls import path

from ccas.views import CcaDetail, CcaList

urlpatterns = [
    path('ccas', CcaList.as_view()),
    path('ccas/<int:pk>', CcaDetail.as_view())
]