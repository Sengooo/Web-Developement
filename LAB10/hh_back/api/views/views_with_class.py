import json

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from api.models import Company, Vacancy
from api.serializers import CompanySerializerS, VacancySerializerS
from django.http.response import JsonResponse


# Create your views here.
class Companies(APIView):
    def get(self, request):
        companies = Company.objects.all()
        serializer = CompanySerializerS(companies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CompanySerializerS(data=request.data)
        if serializer.is_valid():  # only when data ?= data. in the create method we are providing only data
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompanyById(APIView):
    def get_object(self, id):
        try:
            return Company.objects.get(id=id)
        except Company.DoesNotExist as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request, id):
        instance = self.get_object(id)
        serializer = CompanySerializerS(instance)
        return Response(serializer.data)

    def put(self, request, id):
        instance = self.get_object(id)
        serializer = CompanySerializerS(instance=instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        instance = self.get_object(id)
        instance.delete()
        return JsonResponse({'deleted': True})

class VacancyListByCompany(APIView):
    def get_object(self, id):
        try:
            return Company.objects.get(id=id)
        except Company.DoesNotExist as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id):
        instance = self.get_object(id)
        vacancies = Vacancy.objects.all().filter(company = instance)
        serializer = VacancySerializerS(vacancies, many=True)
        return Response(serializer.data)


class Vacancies(APIView):
    def get(self, request):
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializerS(vacancies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VacancySerializerS(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VacancyDetails(APIView):
    def get_object(self, id):
        try:
            return Vacancy.objects.get(id=id)
        except Vacancy.DoesNotExist as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id):
        instance = self.get_object(id)
        serializer = VacancySerializerS(instance)
        return Response(serializer.data)

    def put(self, request, id):
        instance = self.get_object(id)
        serializer = VacancySerializerS(instance=instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        instance = self.get_object(id)
        instance.delete()
        return Response({'deleted': True})


class VacancyTop10(APIView):
    def get(self, request):
        vacancies = Vacancy.objects.all().order_by("-salary")[:10]
        serializer = VacancySerializerS(vacancies, many=True)
        return Response(serializer.data)
