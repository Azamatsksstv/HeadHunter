from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from . import serializers
from . import models


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer


class VacancyViewSet(viewsets.ModelViewSet):
    queryset = models.Vacancy.objects.all()
    serializer_class = serializers.VacancySerializer
    permission_classes = permissions.IsAuthenticatedOrReadOnly,


class CompanyVacancyList(viewsets.ModelViewSet):
    serializer_class = serializers.VacancySerializer
    permission_classes = permissions.IsAuthenticatedOrReadOnly,

    def get_queryset(self):
        company_id = self.kwargs['pk']
        queryset = models.Vacancy.objects.filter(company_id=company_id)
        return queryset


class TopTenVacanciesView(generics.ListAPIView):
    serializer_class = serializers.VacancySerializer

    def get_queryset(self):
        vacancies = models.Vacancy.objects.order_by('-salary')[:10]
        return vacancies
