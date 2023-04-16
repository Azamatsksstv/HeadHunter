from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('companies', views.CompanyViewSet)
router.register('vacancies', views.VacancyViewSet)


urlpatterns = [
    path('companies/<int:pk>/vacancies/', views.CompanyVacancyList.as_view({'get': 'list'})),
    path('vacancies/top_ten/', views.TopTenVacanciesView.as_view()),
    # path('vacancies/<int:id>/submit/', )
]

urlpatterns += router.urls
