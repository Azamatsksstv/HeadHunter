from django.shortcuts import render
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response

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


class SubmitVacancyList(viewsets.ModelViewSet):
    serializer_class = serializers.VacancySerializer

    def get_queryset(self):
        vacancy_id = self.kwargs['id']
        queryset = models.Vacancy.objects.filter(id=vacancy_id)
        print(queryset)
        return queryset

    def send_notification(self):
        return Response({'message': 'Вы успешно отправили запрос на эту вакансию'}, status=status.HTTP_201_CREATED)


class TopTenVacanciesView(generics.ListAPIView):
    serializer_class = serializers.VacancySerializer

    def get_queryset(self):
        vacancies = models.Vacancy.objects.order_by('-salary')[:10]
        return vacancies
