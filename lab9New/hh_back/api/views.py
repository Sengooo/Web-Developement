import json

from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from .models import Vacancy, Company
from .serializers import CompanySerializer, VacancySerializer


# Create your views here.
@csrf_exempt
def companies(request):
    try:
        companies = Company.objects.all()
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, status=400)

    if request.method == 'GET':
        companies_json = [c.to_json() for c in companies]
        return JsonResponse(companies_json, safe=False)
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name', '')
        description = data.get('description', '')
        city = data.get('city', '')
        address = data.get('address', '')
        company = Company.objects.create(name=name, description=description, city=city, address=address)
        return JsonResponse(company.to_json(), safe=False)


@csrf_exempt
def companiesById(request, id):
    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, status=400)
    if request.method == 'GET':
        return JsonResponse(company.to_json(), safe=False, status=200)
    if request.method == 'PUT':
        data = json.loads(request.body)
        name = data.get('name', '')
        description = data.get('description', '')
        city = data.get('city', '')
        address = data.get('address', '')
        company.name = name
        company.description = description
        company.city = city
        company.address = address
        company.save()
        return JsonResponse(company.to_json(), safe=False)
    if request.method == 'DELETE':
        company.delete()
        return JsonResponse({"deleted": True})


def companyIdVacancies(request, id):
    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, status=400)
    vacancies = company.vacancies.all()
    vacancies_json = [v.to_json() for v in vacancies]
    return JsonResponse(vacancies_json, safe=False)
@csrf_exempt
def vacancyList(request):
    try:
        vacancies = Vacancy.objects.all()
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, status=400)

    vacancies_json = [v.to_json() for v in vacancies]
    return JsonResponse(vacancies_json, safe=False)
@csrf_exempt
def vacancyDetail(request, id):
    try:
        vacancy = Vacancy.objects.get(id=id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, status=400)

    if request.method == "GET":
        return JsonResponse(vacancy.to_json())
    if request.method == "DELETE":
        vacancy.delete()
        return JsonResponse({"deleted": True})
    if request.method == 'PUT':
        data = json.loads(request.body)
        name = data.get('name', '')
        description = data.get('description', '')
        salary = data.get('salary', '')

        vacancy.name = name
        vacancy.description = description
        vacancy.salary = salary

        vacancy.save()
        return JsonResponse(vacancy.to_json(), safe=False)

def topTenVacancies(request):
    vacancies = Vacancy.objects.all().order_by('-salary')
    vacancies_json = [v.to_json() for v in vacancies]
    return JsonResponse(vacancies_json, safe=False)
